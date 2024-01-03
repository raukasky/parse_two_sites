from sqlalchemy import Column, Integer, String, Text

from models.mixin import TimestampMixin


class Website(TimestampMixin):
    __tablename__ = 'website'
    __table_args__ = (
        {'schema': 'document'}
    )
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
    )
    domain = Column(
        String,
        nullable=False
    )
    robots_txt = Column(
        String,
        nullable=True
    )
    sitemap = Column(
        String,
        nullable=True
    )
    disallow = Column(
        Text,
        nullable=True
    )

