from pydantic import Field, PositiveFloat
from restaurante.contrib.schema import BaseSchema, Saida
from datetime import datetime
from typing import Literal

class CardapioOut(Saida):
    nome: str
    preco: PositiveFloat
    descricao: str
    
class AdicionarItemCardapio(BaseSchema):
    nome: str
    preco: PositiveFloat
    descricao: str
