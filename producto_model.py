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