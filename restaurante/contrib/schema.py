
from pydantic import BaseModel
from sqlalchemy import DateTime

class BaseSchema(BaseModel):
    class Config:
        orm_mode = True # Converte snake_case para camelCase
        
class Saida(BaseModel):
    id: int
    created_at: DateTime