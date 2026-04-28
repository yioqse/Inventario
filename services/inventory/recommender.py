from typing import List, Dict, Any

def generate_recommendations(products_needing_attention: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Genera recomendaciones de reposición para productos críticos o con stock bajo.

    Esta función evalúa una lista de productos que requieren atención y determina
    la acción a tomar y su prioridad (Alta para agotados, Media para bajos).

    Args:
        products_needing_attention (List[Dict[str, Any]]): Una lista de diccionarios 
            representando los productos que tienen stock crítico o bajo. Cada 
            diccionario debe contener las claves 'producto', 'stock_actual' 
            y preferiblemente 'stock_minimo'.

    Returns:
        List[Dict[str, Any]]: Una lista de diccionarios con las recomendaciones 
        generadas, cada uno conteniendo el 'producto', la 'recomendacion' (texto 
        descriptivo) y la 'prioridad' (ALTA o MEDIA).

    Example:
        >>> productos = [
        ...     {"producto": "Leche", "stock_actual": 0, "stock_minimo": 5},
        ...     {"producto": "Huevos", "stock_actual": 3, "stock_minimo": 10}
        ... ]
        >>> generate_recommendations(productos)
        [
            {'producto': 'Leche', 'recomendacion': '🔄 Reponer urgentemente Leche. Stock agotado.', 'prioridad': 'ALTA'},
            {'producto': 'Huevos', 'recomendacion': '📦 Reponer 17 unidades de Huevos. Stock bajo.', 'prioridad': 'MEDIA'}
        ]
    """
    recommendations = []
    for product in products_needing_attention:
        producto = product["producto"]
        stock_actual = product["stock_actual"]
        stock_minimo = product.get("stock_minimo", 5)
        
        if stock_actual == 0:
            rec = f"🔄 Reponer urgentemente {producto}. Stock agotado."
            prioridad = "ALTA"
        else:
            rec = f"📦 Reponer {stock_minimo * 2 - stock_actual} unidades de {producto}. Stock bajo."
            prioridad = "MEDIA"
            
        recommendations.append({
            "producto": producto, 
            "recomendacion": rec, 
            "prioridad": prioridad
        })
    return recommendations
