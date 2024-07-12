from pydantic import Field
from restaurante.contrib.schema import BaseSchema, Saida
from datetime import datetime
from typing import Literal


class CardapioOut(Saida):
    nome: str
    preco: float
    descricao: str
    
class AdicionarItemCardapio(BaseSchema):
    nome: str
    preco: float
    descricao: str
