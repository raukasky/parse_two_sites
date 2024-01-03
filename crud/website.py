from typing import List

from sqlalchemy.orm import Session

from models import Website
from models.crud import CRUDBase
from schemas import *


class WebsiteCRUD(CRUDBase[Website, WebsiteCreate, WebsiteUpdate]):
    def get_by_domain(self,
                      db: Session,
                      url: str
                      ) -> List[Website] | None:
        result = (db.query(self.model)
                  .filter(self.model.domain == url))
        return WebsiteDetails.model_validate_list(result.all())


website = WebsiteCRUD(Website)
