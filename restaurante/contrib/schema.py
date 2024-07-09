
from datetime import datetime
from pydantic import BaseModel
class BaseSchema(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        
class Saida(BaseModel):
    id: int
    created_at: datetime