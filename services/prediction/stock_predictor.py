from typing import List, Dict, Any, Optional
from services.prediction.demand_analyzer import calculate_daily_demand

def predict_stock_outage(sales_history: List[int], current_stock: int, product_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Predice cuándo se agotará el stock y genera una recomendación.

    Utiliza el historial de ventas para proyectar la duración del stock 
    actual e identificar si el producto se encuentra en un estado crítico.

    Args:
        sales_history (List[int]): Lista de ventas diarias recientes.
        current_stock (int): La cantidad de unidades disponibles actualmente.
        product_info (Optional[Dict[str, Any]], optional): Diccionario con 
            información adicional del producto. Por defecto es None.

    Returns:
        Dict[str, Any]: Un diccionario que contiene:
            - 'dias_hasta_agotarse' (float): Estimación en días.
            - 'cantidad_recomendada' (int): Cantidad a reponer sugerida.
            - 'estado' (str): Clasificación de urgencia.
            - 'consumo_promedio_diario' (float): El consumo ajustado estimado.
            
    Raises:
        ValueError: Si la lista de historial_ventas está vacía.
    """
    if current_stock <= 0:
        return {
            "dias_hasta_agotarse": 0, 
            "cantidad_recomendada": 10, 
            "estado": "AGOTADO ❌",
            "consumo_promedio_diario": 0.0
        }
    
    if not sales_history:
        raise ValueError("El historial de ventas no puede estar vacío para predecir el stock.")
        
    adjusted_daily = calculate_daily_demand(sales_history)
    avg_daily_sales = sum(sales_history) / len(sales_history)
    
    days_until_out = max(0, min(90, round(current_stock / adjusted_daily, 1))) if adjusted_daily > 0 else 999
    
    if days_until_out <= 2:
        estado = "CRÍTICO ⚠️"
    elif days_until_out <= 5:
        estado = "BAJO ⚠️"
    elif days_until_out <= 10:
        estado = "MODERADO ℹ️"
    else:
        estado = "ADECUADO ✅"
    
    return {
        "dias_hasta_agotarse": days_until_out,
        "cantidad_recomendada": round(avg_daily_sales * 10),
        "estado": estado,
        "consumo_promedio_diario": round(adjusted_daily, 2)
    }
