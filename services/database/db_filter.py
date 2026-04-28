from typing import List, Dict, Any
from services.database.db_reader import get_product_info
from services.database.product_db import product_database

def get_sales_history(product_name: str, days: int = 20) -> List[int]:
    """Filtra y devuelve el historial de ventas de un producto específico.

    Args:
        product_name (str): El nombre del producto a consultar.
        days (int, optional): La cantidad de días recientes del historial que se 
            quieren recuperar. Por defecto es 20.

    Returns:
        List[int]: Una lista de enteros representando las ventas diarias del producto.
        Si el producto no existe, devuelve una lista vacía.
    """
    product = get_product_info(product_name)
    if product:
        return product["historial_ventas"][-days:] if days > 0 else product["historial_ventas"]
    return []

def get_by_category(category: str) -> List[Dict[str, Any]]:
    """Filtra productos por categoría.

    Args:
        category (str): El nombre de la categoría a filtrar (ej. 'Bebidas').

    Returns:
        List[Dict[str, Any]]: Una lista de productos (diccionarios) que pertenecen a 
        la categoría especificada.
    """
    return [p for p in product_database.values() if p["categoria"].lower() == category.lower()]
