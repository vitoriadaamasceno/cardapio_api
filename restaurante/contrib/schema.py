
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum as PyEnum
class Status(PyEnum):
    RECEBIDO = "RECEBIDO"
    PREPARANDO = "PREPARANDO"
    EM_ENTREGA = "EM ENTREGA"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"
    ATRASADO = "ATRASADO"

class Role(PyEnum):
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"

class Categoria(PyEnum):
    BEBIDA = "BEBIDA"
    PRATO = "PRATO"
    SOBREMESA = "SOBREMESA"
class BaseSchema(BaseModel):
    class Config:
        str_strip_whitespace = True
        
class Saida(BaseModel):
    id: Optional[int]   