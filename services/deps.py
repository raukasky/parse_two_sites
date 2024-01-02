from sqlalchemy.orm import Session

from core.db import SessionLocal


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
