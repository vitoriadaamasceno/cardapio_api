from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal
from restaurante.contrib.schema import BaseSchema, Saida

class UserClient(BaseSchema):
    nome: str
    email: EmailStr
    senha: str
    telefone: str
    endereco: str

