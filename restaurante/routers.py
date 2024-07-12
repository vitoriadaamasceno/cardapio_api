from fastapi import APIRouter
from restaurante.controllers.cliente.cliente import router as client_router
from restaurante.controllers.login import router as login_router
from restaurante.controllers.cardapio import router as cardapio_router

api_router = APIRouter()
api_router.include_router(client_router, prefix="/client", tags=["client"])
api_router.include_router(login_router, prefix="/login", tags=["login"])
api_router.include_router(cardapio_router, prefix="/cardapio", tags=["cardapio"])
