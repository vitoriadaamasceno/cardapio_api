from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal


class Cardapio(BaseModel):
    id : int
    nome: str
    preco: float
    descricao: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True # Converte snake_case para camelCase
        
class AdicionarItemCardapio(BaseModel):
    nome: str
    preco: float
    descricao: str
    
class AtualizarItemCardapio(BaseModel):
    nome: str | None = None
    preco: float | None = None
    descricao: str | None = None
    created_at: datetime | None = None
    
    class Config:
        orm_mode = True # Converte snake_case para camelCase