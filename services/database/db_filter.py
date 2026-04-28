from typing import List
from services.database.db_reader import get_product_info
from services.database.product_db import product_database

def get_sales_history(product_name: str, days: int = 20) -> List[int]:
    """
    Filtra y devuelve el historial de ventas de un producto específico.
    """
    product = get_product_info(product_name)
    if product:
        return product["historial_ventas"][-days:] if days > 0 else product["historial_ventas"]
    return []

def get_by_category(category: str) -> List[dict]:
    """
    Filtra productos por categoría.
    """
    return [p for p in product_database.values() if p["categoria"].lower() == category.lower()]
