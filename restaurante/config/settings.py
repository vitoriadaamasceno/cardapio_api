from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://cardapio:cardapio@localhost/cardapio') #configura a url do banco de dados

settings = Settings()