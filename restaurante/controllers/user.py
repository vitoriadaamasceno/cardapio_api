from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

#para acessar o banco de dados é necessario acessar a sessão do banco de dados para isso vou criar uma dependencia
@router.post(
    path="/",
    description="criar uma conta de usuário", 
    status_code=201, 
    response_description="Usuário criado com sucesso"
)
async def create_user():
    return {"message": "Hello World"}