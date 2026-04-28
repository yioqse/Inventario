from services.inventory.metrics import count_by_status

def test_count_by_status_all_states():
    """Verifica que se cuenten correctamente los estados CRÍTICO, BAJO y ADECUADO.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = count_by_status([{"nombre": "Leche", "cantidad": 0}])
        >>> result['resumen']['productos_criticos'] == 1
        True
    """
    # Arrange
    detected_products = [
        {"nombre": "Leche", "cantidad": 0},      # Crítico (Agotado)
        {"nombre": "Huevos", "cantidad": 2},     # Bajo (min_stock = 3)
        {"nombre": "Yogur", "cantidad": 20}      # Adecuado (min_stock = 8)
    ]
    
    # Act
    resultado = count_by_status(detected_products)
    
    # Assert
    assert resultado["resumen"]["total_productos"] == 3
    assert resultado["resumen"]["productos_criticos"] == 1
    assert resultado["resumen"]["productos_bajos"] == 1
    assert resultado["resumen"]["productos_adecuados"] == 1

def test_count_by_status_empty_list():
    """Verifica que enviar una lista vacía devuelva contadores en cero.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = count_by_status([])
        >>> result['resumen']['total_productos'] == 0
        True
    """
    # Arrange
    detected_products = []
    
    # Act
    resultado = count_by_status(detected_products)
    
    # Assert
    assert resultado["resumen"]["total_productos"] == 0
    assert resultado["resumen"]["total_unidades"] == 0
    assert resultado["resumen"]["productos_criticos"] == 0
