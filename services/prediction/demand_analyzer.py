from typing import List

def calculate_daily_demand(sales_history: List[int]) -> float:
    """
    Calcula el promedio diario de consumo ajustado por tendencia.
    """
    if not sales_history:
        return 0.0
        
    avg_daily_sales = sum(sales_history) / len(sales_history)
    
    if len(sales_history) >= 5:
        recent_avg = sum(sales_history[-5:]) / 5
        trend_factor = recent_avg / avg_daily_sales if avg_daily_sales > 0 else 1
        adjusted_daily = avg_daily_sales * trend_factor
    else:
        adjusted_daily = avg_daily_sales
        
    return adjusted_daily
