from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_size=25,  # default in SQLAlchemy
    max_overflow=20,  # default in SQLAlchemy
    connect_args={'application_name': settings.PROJECT_NAME},
    echo=settings.POSTGRES_ECHO,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)