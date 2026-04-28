from services.database.product_db import product_database

def test_product_database_size():
    """Verifica que la base de datos contenga exactamente 25 productos.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> len(product_database) == 25
        True
    """
    assert len(product_database) == 25

def test_product_database_categories():
    """Verifica que todos los productos tengan categorías válidas.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> list(product_database.values())[0]["categoria"] in {"Refrigerados", "Conservas", "Bebidas", "Panadería", "Despensa"}
        True
    """
    valid_categories = {"Refrigerados", "Conservas", "Bebidas", "Panadería", "Despensa"}
    for _, product_info in product_database.items():
        assert product_info["categoria"] in valid_categories

def test_product_database_fields():
    """Verifica que cada producto tenga los campos obligatorios.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> "id" in list(product_database.values())[0]
        True
    """
    required_fields = {"id", "nombre", "categoria", "precio", "unidad", "stock_minimo", "stock_maximo", "tiempo_reposicion", "historial_ventas"}
    for _, product_info in product_database.items():
        assert required_fields.issubset(set(product_info.keys()))
