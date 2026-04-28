from services.database.db_reader import get_product_info, get_all_products

def test_get_product_info_valid():
    """Verifica que get_product_info devuelve información correcta para un producto existente.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> product = get_product_info("Leche Entera")
        >>> product["nombre"] == "Leche Entera"
        True
    """
    product = get_product_info("Leche Entera")
    assert product is not None
    assert product["nombre"] == "Leche Entera"
    assert product["categoria"] == "Refrigerados"

def test_get_product_info_invalid():
    """Verifica que get_product_info devuelve None para un producto inexistente.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> product = get_product_info("Producto Inexistente XYZ")
        >>> product is None
        True
    """
    product = get_product_info("Producto Inexistente XYZ")
    assert product is None

def test_get_all_products():
    """Verifica que get_all_products devuelve una lista con todos los productos de la base de datos.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> products = get_all_products()
        >>> len(products) == 25
        True
    """
    products = get_all_products()
    assert isinstance(products, list)
    assert len(products) == 25
