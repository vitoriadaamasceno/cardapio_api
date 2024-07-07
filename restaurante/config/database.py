from typing import AsyncGenerator #importando o AsyncGenerator para poder usar no banco de dados

#iremos criar a sessão do banco de dados para poder fazer as consultas
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from restaurante.config.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True) #criando a engine do banco de dados
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False #expirando a sessão após o commit e criando a class AsyncSession para poder usar o AsyncGenerator
) #criando a sessão do banco de dados

async def get_session() -> AsyncGenerator[AsyncSession, None]: #criando a função get_session para poder pegar a sessão do banco de dados
    async with async_session() as session: #criando a sessão do banco de dados
        yield session
        