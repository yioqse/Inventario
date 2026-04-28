from services.database.db_filter import get_sales_history, get_by_category

def test_get_sales_history_valid():
    """Verifica que se devuelva el historial de ventas para un producto válido."""
    history = get_sales_history("Leche", days=5)
    assert isinstance(history, list)
    assert len(history) == 5

def test_get_sales_history_invalid_product():
    """Verifica que se devuelva una lista vacía para un producto inexistente."""
    history = get_sales_history("Producto Inexistente XYZ")
    assert isinstance(history, list)
    assert len(history) == 0

def test_get_by_category_valid():
    """Verifica el filtrado por categoría válido."""
    beverages = get_by_category("Bebidas")
    assert len(beverages) == 5
    for item in beverages:
        assert item["categoria"] == "Bebidas"

def test_get_by_category_invalid():
    """Verifica el filtrado por una categoría que no existe."""
    items = get_by_category("Electrónica")
    assert isinstance(items, list)
    assert len(items) == 0

def test_get_by_category_case_insensitive():
    """Verifica que el filtrado por categoría no distingue mayúsculas de minúsculas."""
    items_upper = get_by_category("BEBIDAS")
    items_lower = get_by_category("bebidas")
    assert len(items_upper) == 5
    assert len(items_lower) == 5
