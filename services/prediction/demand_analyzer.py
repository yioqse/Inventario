from typing import List

def calculate_daily_demand(sales_history: List[int]) -> float:
    """Calcula el promedio diario de consumo ajustado por tendencia.

    Args:
        sales_history (List[int]): Historial de ventas diarias del producto.

    Returns:
        float: El consumo diario estimado, ponderando las ventas recientes 
        para detectar tendencias si hay suficientes datos.

    Raises:
        ValueError: Si la lista de historial_ventas está vacía.
    """
    if not sales_history:
        raise ValueError("El historial de ventas no puede estar vacío.")
        
    avg_daily_sales = sum(sales_history) / len(sales_history)
    
    if len(sales_history) >= 5:
        recent_avg = sum(sales_history[-5:]) / 5
        trend_factor = recent_avg / avg_daily_sales if avg_daily_sales > 0 else 1
        adjusted_daily = avg_daily_sales * trend_factor
    else:
        adjusted_daily = avg_daily_sales
        
    return adjusted_daily
