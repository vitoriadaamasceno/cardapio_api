from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class User(BaseModel):
    id : int
    password: str
    email: EmailStr
    tel: str
    role: Literal["ADMIN", "CLIENT"] = Field(default="CLIENT")
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True # Converte snake_case para camelCase

class CriarUsuario(BaseModel):
    email: EmailStr
    password: str
    tel: str
    

class AtualizarUsuario(BaseModel):
    password: str | None = None
    email: EmailStr | None = None
    role: Literal["admin", "client"] | None = None
