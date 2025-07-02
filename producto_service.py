from producto_model import Producto

# Base de datos en memoria
productos_db = []
next_id = 1

def agregar_producto(producto: Producto):
    """
    Agrega un nuevo producto a la base de datos.

    Args:
        producto (Producto): Objeto que contiene los datos del producto (nombre y precio).
    """
    global next_id
    producto.id = next_id
    productos_db.append(producto)
    next_id += 1
    return producto

def listar_productos():
    """
    Obtiene la lista de todos los productos almacenados en la base de datos.

    Returns:
        list[Producto]: Lista de productos.
    """
    return productos_db

def dame_producto_por_id(id: int):
    """
    Obtiene un producto por su ID.
    
    Args:
        id (int): ID del producto a buscar.
        
    Returns:
        Producto | None: El producto encontrado o None si no existe.
    """
    for producto in productos_db:
        if producto.id == id:
            return producto
    return None

def modificar_producto(id: int, producto_actualizado: Producto):
    """
    Modifica un producto existente.
    
    Args:
        id (int): ID del producto a modificar.
        producto_actualizado (Producto): Datos actualizados del producto.
        
    Returns:
        Producto | None: El producto modificado o None si no existe.
    """
    for i, producto in enumerate(productos_db):
        if producto.id == id:
            producto_actualizado.id = id
            productos_db[i] = producto_actualizado
            return producto_actualizado
    return None

def eliminar_producto(id: int):
    """
    Elimina un producto por su ID.
    
    Args:
        id (int): ID del producto a eliminar.
        
    Returns:
        bool: True si se eliminó correctamente, False si no se encontró.
    """
    for i, producto in enumerate(productos_db):
        if producto.id == id:
            del productos_db[i]
            return True
    return False
