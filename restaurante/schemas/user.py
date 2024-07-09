from datetime import datetime
from typing import Any, Literal, Optional
from restaurante.contrib.schema import BaseSchema, Saida
from pydantic import ValidationError, model_validator, field_validator
from restaurante.utils.authenticator import Authenticator
from enum import Enum 

class Role(str,Enum):
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"
class UserClient(BaseSchema):
    email: str
    senha: str
    nome: str
    endereco: str
    telefone: str

    @field_validator("senha")
    @classmethod
    def hash_password(cls, senha: str) -> str:
        authenticator = Authenticator()
        return authenticator.hash_password(senha)

class UserLogin(BaseSchema):
    email: str
    senha: str
    
class UserUpdate(BaseSchema):
    email: Optional[str]
    nome: Optional[str]
    endereco: Optional[str]
    telefone: Optional[str]

class UserResponse(Saida):
    detail: str