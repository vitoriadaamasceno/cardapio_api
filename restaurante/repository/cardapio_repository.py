from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from restaurante.models.models import Cardapio


class CardapioRepository:
    # uso do scalars: o scalars é um metodo que transforma o resultado em um objeto, no caso, um objeto do tipo Cardapio
    #serao usados metodos estaticos para que não seja necessario instanciar a classe, pois não será necessario instanciar a class
    @staticmethod
    async def create_item_cardapio(db_session: AsyncSession, cardapio:Cardapio) -> Cardapio:
        db_session.add(cardapio) #adciona o model ao banco
        await db_session.commit() # commmita = sobe essa mudança
        await db_session.refresh(cardapio) #reinicia o banco
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