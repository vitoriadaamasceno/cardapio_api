from datetime import datetime
from typing import Literal
from restaurante.contrib.schema import BaseSchema, Saida


class Role(BaseSchema):
    ADMIN: Literal["ADMIN"]
    CLIENT: Literal["CLIENT"]
class UserClient(BaseSchema):
    email: str
    senha: str
    nome: str
    endereco: str
    telefone: str
