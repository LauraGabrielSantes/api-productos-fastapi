from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from producto_model import Producto
from producto_service import (
    agregar_producto,
    listar_productos, 
    dame_producto_por_id,
    modificar_producto,
    eliminar_producto
)

app = FastAPI(
    title="API de Productos :)",
    description="API REST para gestionar productos con operaciones CRUD",
    version="1.0.0"
)

class ProductoCreate(BaseModel):
    """Modelo para crear un producto (sin ID)"""
    nombre: str
    precio: float
class ProductoUpdate(BaseModel):
    """Modelo para actualizar un producto (sin ID)"""
    nombre: str
    precio: float
@app.get("/productos", response_model=List[Producto])
def obtener_productos():
    """
    Obtiene la lista de todos los productos.
    
    Returns:
        List[Producto]: Lista de todos los productos.
    """
    return listar_productos()

@app.get("/productos/{id}", response_model=Producto)
def obtener_producto(id: int):
    """
    Obtiene un producto específico por su ID.
    
    Args:
        id (int): ID del producto a buscar.
        
    Returns:
        Producto: El producto encontrado.
        
    Raises:
        HTTPException: Si el producto no existe.
    """
    producto = dame_producto_por_id(id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos", response_model=Producto, status_code=201)
def crear_producto(producto_data: ProductoCreate):
    """
    Crea un nuevo producto.
    
    Args:
        producto_data (ProductoCreate): Datos del producto a crear.
        
    Returns:
        Producto: El producto creado con su ID asignado.
    """
   
    producto = Producto(
        id=0,  
        nombre=producto_data.nombre,
        precio=producto_data.precio
    )
    return agregar_producto(producto)

@app.put("/productos/{id}", response_model=Producto)
def actualizar_producto(id: int, producto_data: ProductoUpdate):
    """     
    Raises:
        HTTPException: Si el producto no existe.
    """
    producto_actualizado = Producto(
        id=id,
        nombre=producto_data.nombre,
        precio=producto_data.precio
    )
    
    resultado = modificar_producto(id, producto_actualizado)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return resultado

@app.delete("/productos/{id}")
def eliminar_producto_endpoint(id: int):
    """
    Elimina un producto.
    
        dict: Mensaje de confirmación.
        
    Raises:
        HTTPException: Si el producto no existe.
    """
    if not eliminar_producto(id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": f"Producto con ID {id} eliminado correctamente"}

@app.get("/")
def root():
    """
    Endpoint raíz de la API.
    
    Returns:
        dict: Mensaje de bienvenida.
    """
    return {"message": "API de Productos"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
