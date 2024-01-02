from sqlalchemy.orm import Session


class BaseDBService(object):

    def __init__(self, db: Session):
        self.db = db
