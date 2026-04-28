from services.inventory.valuation import calculate_inventory_value

def test_calculate_inventory_value_correct():
    """Verifica que el cálculo del valor total sea precio x stock.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = calculate_inventory_value([{"nombre": "Leche", "cantidad": 10}])
        >>> result == 12.0
        True
    """
    # Arrange
    detected_products = [
        {"nombre": "Leche", "cantidad": 10},   # precio 1.20 -> 12.0
        {"nombre": "Huevos", "cantidad": 2}    # precio 2.50 -> 5.0
    ]
    
    # Act
    resultado = calculate_inventory_value(detected_products)
    
    # Assert
    assert resultado == 17.0

def test_calculate_inventory_value_not_in_db():
    """Verifica que un producto no existente en la BD no sume al valor.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = calculate_inventory_value([{"nombre": "Falso", "cantidad": 10}])
        >>> result == 0.0
        True
    """
    # Arrange
    detected_products = [
        {"nombre": "Producto Inexistente", "cantidad": 100}
    ]
    
    # Act
    resultado = calculate_inventory_value(detected_products)
    
    # Assert
    assert resultado == 0.0

def test_calculate_inventory_value_empty():
    """Verifica que una lista vacía retorne 0.0.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = calculate_inventory_value([])
        >>> result == 0.0
        True
    """
    # Arrange
    detected_products = []
    
    # Act
    resultado = calculate_inventory_value(detected_products)
    
    # Assert
    assert resultado == 0.0
