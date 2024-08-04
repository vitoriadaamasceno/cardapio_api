from fastapi import APIRouter
from restaurante.controllers.cliente import router as client_router
from restaurante.controllers.login import router as login_router
from restaurante.controllers.cardapio import router as cardapio_router
from restaurante.controllers.pedido import router as pedido_router

api_router = APIRouter()
api_router.include_router(client_router, prefix="/client", tags=["client"])
api_router.include_router(login_router, prefix="/login", tags=["login"])
api_router.include_router(cardapio_router, prefix="/cardapio", tags=["cardapio"])
api_router.include_router(pedido_router, prefix="/pedido", tags=["pedido"])