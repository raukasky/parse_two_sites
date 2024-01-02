import json
from typing import Any, Generic, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        :return: CRUD record to table
        """
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()  # noqa

    def get_multi(
            self,
            db: Session,
    ) -> Any:
        return db.query(self.model).all()

    def create(
            self,
            db: Session,
            *,
            obj_in: CreateSchemaType,
            commit: bool = True,
    ) -> ModelType:
        obj_in_data = json.dumps(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        if commit:
            db.commit()
            db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
        commit: bool = True,
    ) -> ModelType:
        obj_data = json.dumps(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        if commit:
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, obj_id: int) -> ModelType:
        obj = db.query(self.model).get(obj_id)
        db.delete(obj)
        db.commit()
        return obj

    @staticmethod
    def remove_by_obj(db: Session, *, db_obj: ModelType) -> ModelType:
        db.delete(db_obj)
        db.commit()
        return db_obj

    @staticmethod
    def create_instance(db: Session,
                        obj: ModelType) -> ModelType:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def bulk_create(db: Session,
                    objs: list[ModelType],
                    commit: bool = True) -> list[ModelType]:
        db.bulk_save_objects(objs)
        if commit:
            db.commit()
        return objs
