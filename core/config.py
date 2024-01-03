from __future__ import annotations
from enum import Enum
from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):

    class Environment(str, Enum):
        local = 'local'
        dev = 'dev'
        prod = 'prod'

    # Environment settings
    ENVIRONMENT: Environment  # local, dev, prod
    COUNTRY_ISO: str = 'KZ'

    # Database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_ECHO: bool
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    # Celery settings
    CELERY_BROKER_URL: str
    CELERY_BACKEND_URL: str

    @field_validator('SQLALCHEMY_DATABASE_URI', mode='after')
    def assemble_db_connection(cls, v: str, values: FieldValidationInfo) -> str:
        if v is not None:
            if isinstance(v, str):
                return v
        return str(PostgresDsn.build(
            scheme="postgresql",
            port=values.data.get("POSTGRES_PORT"),
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        ))


settings = Settings()
