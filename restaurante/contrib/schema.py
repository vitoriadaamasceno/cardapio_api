
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class BaseSchema(BaseModel):
    class Config:
        str_strip_whitespace = True
        
class Saida(BaseModel):
    id: Optional[int]   