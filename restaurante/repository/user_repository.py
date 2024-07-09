from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from restaurante.models.models import Usuario


class UserRepository:
    
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
        ).scalars().first()