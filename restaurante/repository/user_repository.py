from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from restaurante.models.models import Usuario


class UserRepository:
    #serao usados metodos estaticos para que não seja necessario instanciar a classe, pois não será necessario instanciar a class
    @staticmethod
    async def create_user(db_session: AsyncSession, user: Usuario) -> Usuario:
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        return user
    
    
    @staticmethod
    async def get_user_by_email(db_session: AsyncSession, email: str) -> Usuario:
        return (await db_session.execute(
            select(Usuario).filter_by(email=email))
        ).scalars().first() #scarlars é um metodo que retorna um objeto do tipo Usuario e o first() retorna o primeiro objeto encontrado
    