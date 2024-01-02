from sqlalchemy import Column, DateTime, func
from .base import Base


class DeleteMixin(Base):
    __abstract__ = True
    deleted_at = Column(DateTime, nullable=True)


class TimestampMixin(Base):
    __abstract__ = True
    created_at = Column(DateTime,
                        nullable=False,
                        server_default=func.now())
    updated_at = Column(DateTime,
                        nullable=False,
                        server_default=func.now(),
                        onupdate=func.now())
