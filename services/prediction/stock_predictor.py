from typing import List, Dict, Any
from services.prediction.demand_analyzer import calculate_daily_demand

def predict_stock_outage(sales_history: List[int], current_stock: int, product_info: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Predice cuándo se agotará el stock y genera una recomendación basada en el historial de ventas.
    """
    if not sales_history or current_stock <= 0:
        return {
            "dias_hasta_agotarse": 0, 
            "cantidad_recomendada": 10, 
            "estado": "AGOTADO" if current_stock <= 0 else "SIN HISTORIAL"
        }
    
    adjusted_daily = calculate_daily_demand(sales_history)
    avg_daily_sales = sum(sales_history) / len(sales_history) if sales_history else 0
    
    days_until_out = max(0, min(90, round(current_stock / adjusted_daily, 1))) if adjusted_daily > 0 else 999
    
    if days_until_out <= 2:
        estado = "CRÍTICO ⚠️"
    elif days_until_out <= 5:
        estado = "BAJO ⚠️"
    elif days_until_out <= 10:
        estado = "MODERADO ℹ️"
    else:
        estado = "ADEQUADO ✅"
    
    return {
        "dias_hasta_agotarse": days_until_out,
        "cantidad_recomendada": round(avg_daily_sales * 10),
        "estado": estado,
        "consumo_promedio_diario": round(adjusted_daily, 2)
    }
