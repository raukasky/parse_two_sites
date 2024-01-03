from typing import Any

from pydantic import BaseModel


class ModelValidateListMixin(BaseModel):

    @classmethod
    def model_validate_list(cls, items: list[Any]) -> list[Any]:
        return [cls.model_validate(item) for item in items]
