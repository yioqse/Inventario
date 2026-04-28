from typing import List, Dict, Any
from services.database.product_db import product_database

def calculate_inventory_value(detected_products: List[Dict[str, Any]]) -> float:
    """
    Calcula el valor total del inventario basándose en los productos detectados.
    """
    total_value = 0.0
    for detected in detected_products:
        product_info = product_database.get(detected["nombre"])
        if product_info and "precio" in product_info:
            total_value += detected["cantidad"] * product_info["precio"]
    return round(total_value, 2)
