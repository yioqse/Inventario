import pytest
from services.vision.detector import detect_products
from services.database.db_reader import get_product_info
from services.database.db_filter import get_sales_history
from services.prediction.stock_predictor import predict_stock_outage
from services.inventory.recommender import generate_recommendations

def test_full_pipeline_end_to_end():
    """Verifica que el flujo de datos completo se ejecute sin excepciones.

    El pipeline simulado es: detección -> obtención de BD -> predicción -> recomendación.
    
    Args: Ninguno.
    Returns: None.
    Example:
        >>> test_full_pipeline_end_to_end() # Ejecuta sin lanzar errores
    """
    # Arrange
    # Iniciamos el flujo llamando al detector (tomará un escenario aleatorio por defecto)
    productos_para_recomendar = []
    excepcion_lanzada = False
    
    # Act
    try:
        deteccion = detect_products()
        productos_detectados = deteccion.get("productos", [])

        for producto_detectado in productos_detectados:
            nombre = producto_detectado["nombre"]
            stock_actual = producto_detectado["cantidad"]
            producto_info = get_product_info(nombre)
            
            if producto_info:
                historial_ventas = get_sales_history(nombre, days=30)
                try:
                    prediccion = predict_stock_outage(historial_ventas, stock_actual, producto_info)
                except ValueError:
                    prediccion = {"estado": "SIN HISTORIAL"}
                
                # Agregamos los productos bajos en stock a la lista de recomendación
                stock_minimo = producto_info.get("stock_minimo", 5)
                if stock_actual <= stock_minimo:
                    productos_para_recomendar.append({
                        "producto": nombre,
                        "stock_actual": stock_actual,
                        "stock_minimo": stock_minimo
                    })
        
        # Ejecutamos el recomendador final
        recomendaciones = generate_recommendations(productos_para_recomendar)

    except Exception as e:
        excepcion_lanzada = True

    # Assert
    assert not excepcion_lanzada, "El pipeline completo no debe lanzar excepciones no controladas"
    assert isinstance(deteccion, dict), "La detección debe retornar un diccionario"
    assert "productos" in deteccion, "El resultado de detección debe contener la clave 'productos'"
    assert isinstance(recomendaciones, list), "El recomendador debe retornar una lista"
