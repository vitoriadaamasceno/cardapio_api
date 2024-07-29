from typing import Annotated 
from fastapi import Depends # o Depends é uma função que permite que você defina dependências, que são objetos que devem ser injetados em um manipulador de rota
from sqlalchemy.ext.asyncio import AsyncSession # vai ser o tipo da dependência que vamos criar
from restaurante.config.database import get_session #importando a função get_session para poder pegar a sessão do banco de dados

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)] #criando a dependencia do banco de dados onde o AsyncSession é a sessão do banco de dados e o Depends é a função que pega a sessão do banco de dados