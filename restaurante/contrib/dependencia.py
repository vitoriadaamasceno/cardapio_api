from typing import Annotated #importando o Annotated para poder usar no banco de dados
from fastapi import Depends #importando o Depends para poder usar no banco de dados transformando em dependencia

from sqlalchemy.ext.asyncio import AsyncSession #importando o AsyncSession para poder usar no banco de dados
from restaurante.config.database import get_session #importando a função get_session para poder pegar a sessão do banco de dados

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)] #criando a dependencia do banco de dados