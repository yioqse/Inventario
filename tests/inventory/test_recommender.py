from services.inventory.recommender import generate_recommendations

def test_generate_recommendations_critical():
    """Verifica que un producto agotado genere recomendación URGENTE (ALTA).

    Args: Ninguno.
    Returns: None.
    Example:
        >>> recs = generate_recommendations([{"producto": "Leche", "stock_actual": 0, "stock_minimo": 5}])
        >>> recs[0]["prioridad"] == "ALTA"
        True
    """
    # Arrange
    products = [
        {"producto": "Agua", "stock_actual": 0, "stock_minimo": 15}
    ]
    
    # Act
    recs = generate_recommendations(products)
    
    # Assert
    assert len(recs) == 1
    assert recs[0]["prioridad"] == "ALTA"
    assert "urgent" in recs[0]["recomendacion"].lower() or "agotado" in recs[0]["recomendacion"].lower()

def test_generate_recommendations_low_stock():
    """Verifica que un producto bajo en stock genere recomendación MEDIA.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> recs = generate_recommendations([{"producto": "Huevos", "stock_actual": 2, "stock_minimo": 5}])
        >>> recs[0]["prioridad"] == "MEDIA"
        True
    """
    # Arrange
    products = [
        {"producto": "Agua", "stock_actual": 5, "stock_minimo": 15}
    ]
    
    # Act
    recs = generate_recommendations(products)
    
    # Assert
    assert len(recs) == 1
    assert recs[0]["prioridad"] == "MEDIA"
