from fastapi import APIRouter, Body, status, HTTPException

from restaurante.contrib.dependencia import DatabaseDependency
from restaurante.schemas.cardapio import AdicionarItemCardapio, CardapioOut 
from restaurante.repository.cardapio_repository import CardapioRepository
from restaurante.models.models import Cardapio


router = APIRouter()

@router.post(
    path="",
    description="Inserir item no cardápio", 
    status_code=status.HTTP_200_OK,
    response_description="Item inserido com sucesso",
)
async def add_cardapio(
    db_session: DatabaseDependency,
    cardapio : AdicionarItemCardapio = Body(...)
):
    nome = cardapio.nome
    descricao = cardapio.descricao
    preco = cardapio.preco
    
    try:
        cardapio = Cardapio(
            name=nome,
            description=descricao,
            price=preco
        )
        cardapio = await CardapioRepository.create_item_cardapio(db_session, cardapio)
        return cardapio
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
        