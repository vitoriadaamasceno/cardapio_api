from fastapi import APIRouter, Body, status, HTTPException
from restaurante.contrib.dependencia import DatabaseDependency
from restaurante.repository.pedido_repository import PedidoRepository

router = APIRouter()    

