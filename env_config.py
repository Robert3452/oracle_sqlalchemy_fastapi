from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ORACLEDB_HOST: str
    ORACLEDB_PORT: int
    ORACLEDB_PASSWORD: str
    ORACLEDB_SID: str
    ORACLEDB_USER: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()
