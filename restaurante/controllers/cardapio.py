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
    
    name_exists = await CardapioRepository.get_cardapio_by_name(db_session, nome)
    if name_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome já cadastrado"
        )
    
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

  
@router.get(
    path="",
    description="Mostrar todos os items no cardapio", 
    status_code=status.HTTP_200_OK
)
async def get_all_cardapio(
    db_session: DatabaseDependency
):
    try:
        cardapio_get_all = await CardapioRepository.get_cardapio(db_session)
        return cardapio_get_all
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )