from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from restaurante.models.models import Cardapio


class CardapioRepository:
    #serao usados metodos estaticos para que não seja necessario instanciar a classe, pois não será necessario instanciar a class
    @staticmethod
    async def create_item_cardapio(db_session: AsyncSession, cardapio:Cardapio) -> Cardapio:
        db_session.add(cardapio)
        await db_session.commit()
        await db_session.refresh(cardapio)
        return cardapio
    
    @staticmethod
    async def get_cardapio(db_session: AsyncSession) -> list[Cardapio]:
        seletor = select(Cardapio)
        result = await db_session.execute(seletor)
        return result.scalars().all()
    
    @staticmethod
    async def get_cardapio_by_name(db_session: AsyncSession, name:str) -> Cardapio:
        seletor = select(Cardapio).where(Cardapio.name == name)
        result = await db_session.execute(seletor)
        return result.scalars().first()