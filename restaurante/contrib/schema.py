
from datetime import datetime
from pydantic import BaseModel
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True # Converte snake_case para camelCase
        
class Saida(BaseModel):
    id: int
    created_at: datetime