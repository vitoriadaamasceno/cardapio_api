from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy.future import select

from restaurante.contrib.dependencia import DatabaseDependency
from restaurante.schemas.user import UserClient, Role
from restaurante.models.models import Usuario

router = APIRouter()

#para acessar o banco de dados é necessario acessar a sessão do banco de dados para isso vou criar uma dependencia
@router.post(
    path="/",
    description="criar uma conta de usuário", 
    status_code=status.HTTP_201_CREATED, 
    response_description="Usuário criado com sucesso"
)
async def create_user(
    db_session: DatabaseDependency, 
    client: UserClient = Body(...)
):
    nome = client.nome
    email_user= client.email
    senha= client.senha
    telefone= client.telefone
    endereco= client.endereco
    
    email_exists = (await db_session.execute(
        select(Usuario).filter_by(email=email_user))
    ).scalars().first()
    
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    try:
        user = Usuario(
            name=nome,
            email=email_user,
            password=senha,
            role=Role.CLIENT,
            tel=telefone,
            address=endereco
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        
        return user
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
    