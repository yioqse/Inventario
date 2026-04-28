import pytest
from services.prediction.demand_analyzer import calculate_daily_demand

def test_calculate_daily_demand_con_historial_normal():
    """Verifica que la demanda diaria se calcula correctamente.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = calculate_daily_demand([3, 4, 5])
        >>> result == 4.0
        True
    """
    # Arrange
    historial = [3, 4, 5, 4, 3, 5, 4, 3, 4, 5]

    # Act
    resultado = calculate_daily_demand(historial)

    # Assert
    assert resultado == 4.0

def test_calculate_daily_demand_un_elemento():
    """Verifica el cálculo de demanda cuando el historial tiene un solo elemento.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> result = calculate_daily_demand([10])
        >>> result == 10.0
        True
    """
    # Arrange
    historial = [10]

    # Act
    resultado = calculate_daily_demand(historial)

    # Assert
    assert resultado == 10.0

def test_calculate_daily_demand_lista_vacia():
    """Verifica que se levante ValueError si el historial está vacío.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> calculate_daily_demand([]) # Lanza ValueError
    """
    # Arrange
    historial = []

    # Act & Assert
    with pytest.raises(ValueError, match="El historial de ventas no puede estar vacío"):
        calculate_daily_demand(historial)
