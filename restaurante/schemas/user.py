from typing import Any, Literal, Optional
from restaurante.contrib.schema import BaseSchema, Saida
from pydantic import field_validator, EmailStr, Field
from restaurante.utils.authenticator import Authenticator
from enum import Enum 

class Role(str,Enum):
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"
class UserClient(BaseSchema):
    email: EmailStr
    senha: str = Field(None, min_length=6, max_length=20)
    nome: str
    endereco: str
    telefone: str = Field(None, min_length=11, max_length=11)

    @field_validator("senha")
    @classmethod
    def hash_password(cls, senha: str) -> str:
        authenticator = Authenticator()
        return authenticator.hash_password(senha)

class UserLogin(BaseSchema):
    email: EmailStr
    senha: str = Field(None, min_length=6, max_length=20)
class UserResponse(Saida):
    detail: Optional[str]