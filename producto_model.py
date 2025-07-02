from pydantic import BaseModel

class Producto(BaseModel):
    """
    Modelo de datos para representar un producto.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
    """
    id: int
    nombre: str
    precio: float

class ProductoCreate(BaseModel):
    """Modelo para crear un producto (sin ID)"""
    id: int
    nombre: str
    precio: float
class ProductoUpdate(BaseModel):
    """Modelo para actualizar un producto (sin ID)"""
    id: int
    nombre: str
    precio: float