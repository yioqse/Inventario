from typing import Optional, List, Dict, Any
from services.database.product_db import product_database

def get_product_info(product_name: str) -> Optional[Dict[str, Any]]:
    """Obtiene la información de un producto por su nombre.

    Args:
        product_name (str): El nombre del producto a buscar.

    Returns:
        Optional[Dict[str, Any]]: Un diccionario con los datos del producto, 
        o None si el producto no existe en la base de datos.
    """
    return product_database.get(product_name, None)

def get_all_products() -> List[Dict[str, Any]]:
    """Devuelve la lista completa de todos los productos en la base de datos.

    Returns:
        List[Dict[str, Any]]: Una lista de diccionarios, donde cada diccionario
        representa un producto con toda su información.
    """
    return list(product_database.values())
