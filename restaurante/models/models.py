from sqlalchemy import Integer, String, Float, Enum, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from restaurante.contrib.schema import Role, Status, Categoria

""" 
Entendendo a doc sqlalchemy:
    - Mapped é um tipo de dado que é usado para mapear um campo de uma tabela do banco de dados
    - mapped_column é uma função que mapeia um campo de uma tabela do banco de dados para um campo de uma classe
    - relationship cria a relação entre as tabelas do banco de dados
"""
class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuario"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[Role] = mapped_column(Enum(Role), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    tel: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())

    #pedidos: Mapped[list["Pedido"]] = relationship("Pedido", back_populates="usuario")

class Pedido(Base):
    __tablename__ = "pedidos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.RECEBIDO)
    total: Mapped[float] = mapped_column(Float)
    delivery_time: Mapped[int] = mapped_column(Integer, default=50)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="pedidos")
    items: Mapped[list["ItemPedido"]] = relationship("ItemPedido", back_populates="pedido")

class Cardapio(Base):
    __tablename__ = "cardapio"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    categoria: Mapped[Categoria] = mapped_column(Enum(Categoria), default=Categoria.PRATO)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())

class ItemPedido(Base):
    __tablename__ = "item_pedido"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=func.now())

    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"))
    cardapio_id: Mapped[int] = mapped_column(ForeignKey("cardapio.id"))
    pedido: Mapped["Pedido"] = relationship("Pedido", back_populates="items")
    cardapio: Mapped["Cardapio"] = relationship("Cardapio")
