from typing import List, Dict, Any

def generate_recommendations(products_needing_attention: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Genera recomendaciones de reposición para productos críticos o con stock bajo.
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
