from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class Pedido(BaseModel):
    id : int
    id_cliente: int
    total: float
    descricao: str
    troco: float
    status: Literal["RECEBIDO", "PREPARANDO", "EM ENTREGA", "ENTREGUE", "CANCELADO", "ATRASADO"]
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True # Converte snake_case para camelCase
        
