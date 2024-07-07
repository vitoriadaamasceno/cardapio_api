from fastapi import FastAPI
from restaurante.router import api_router as router

app = FastAPI(title="Cardapio API", description="API para cardapio de restaurante", version="1.0")
app.include_router(router, prefix="")