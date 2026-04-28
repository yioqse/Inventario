from typing import Optional, List, Dict, Any
from services.database.product_db import product_database

def get_product_info(product_name: str) -> Optional[Dict[str, Any]]:
    """
    Obtiene la información de un producto por su nombre.
    """
    return product_database.get(product_name, None)

def get_all_products() -> List[Dict[str, Any]]:
    """
    Devuelve la lista completa de todos los productos en la base de datos.
    """
    return list(product_database.values())
