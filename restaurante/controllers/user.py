from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy.future import select

from restaurante.contrib.dependencia import DatabaseDependency
from restaurante.schemas.user import UserClient, Role, UserResponse
from restaurante.models.models import Usuario
from restaurante.repository.user_repository import UserRepository

router = APIRouter()

#para acessar o banco de dados é necessario acessar a sessão do banco de dados para isso vou criar uma dependencia
@router.post(
    path="/",
    description="criar uma conta de usuário", 
    status_code=status.HTTP_201_CREATED, 
    response_model=UserResponse
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
    
    email_exists = await UserRepository.get_user_by_email(db_session, email_user)
    
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
        
        await UserRepository.create_user(db_session, user)
        
        return UserResponse(
            id=user.id,
            detail="Usuário criado com sucesso",
            created_at=user.created_at
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
    