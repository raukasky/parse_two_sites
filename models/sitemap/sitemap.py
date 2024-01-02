from sqlalchemy import Column, Integer

from models.mixin import TimestampMixin


class Sitemap(TimestampMixin):
    __tablename__ = 'sitemap'
    __table_args__ = (
        {'schema': 'base'}
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
    )
