from typing import Union
from pydantic import BaseModel

from schemas.base import ModelValidateListMixin


class WebsiteBase(BaseModel):
    domain: str
    robots_txt: Union[str, None]
    sitemap: Union[str, None]
    disallow: Union[str, None]

    class Config:
        from_attributes = True


class WebsiteCreate(WebsiteBase):
    pass


class WebsiteUpdate(WebsiteBase):
    id: int


class WebsiteDetails(WebsiteBase, ModelValidateListMixin):
    id: int


class WebsiteDetail(WebsiteBase):
    id: int
