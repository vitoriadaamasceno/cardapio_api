from fastapi import APIRouter, Body, status, HTTPException

from restaurante.contrib.dependencia import DatabaseDependency
from restaurante.schemas.user import UserResponse, UserLogin
from restaurante.models.models import Usuario
from restaurante.repository.user_repository import UserRepository
from restaurante.utils.authenticator import Authenticator

router = APIRouter()

@router.post(
    path="",
    description="Login de usuário", 
    status_code=status.HTTP_200_OK, 
    response_model=UserResponse
)
async def login(
    db_session: DatabaseDependency,
    client: UserLogin = Body(...)
):
    email_user= client.email
    senha= client.senha

    user = await UserRepository.get_user_by_email(db_session, email_user)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email não cadastrado"
        )
        
    authenticator = Authenticator()
    user_password = user.password
    is_valid = authenticator.verify_password(senha, user_password)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credentais inválidas"
        )
    try: #se o usuario for encontrado e a senha for valida try nao permite que o codigo seja executado caso ocorra um erro
        return UserResponse(
            id=user.id,
            detail="Usuário logado com sucesso",
            
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )