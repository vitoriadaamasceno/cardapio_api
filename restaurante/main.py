from fastapi import FastAPI
from restaurante.routers import api_router

app = FastAPI(title="Cardapio API", description="API para cardapio de restaurante", version="1.0")
app.include_router(api_router, prefix="")