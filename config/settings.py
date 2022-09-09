from pydantic import BaseSettings, Extra


class AppSettings(BaseSettings):
    port: int
    example: str

    class Config:
        extra = Extra.ignore
        env_file = '.env'
        env_file_encoding = 'utf-8'
