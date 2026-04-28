import pytest
from unittest.mock import patch
from services.prediction.stock_predictor import predict_stock_outage

def test_predict_stock_outage_mock_demand():
    """Verifica que los días y el estado sean correctos aislando la demanda con un mock.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> with patch('services.prediction.stock_predictor.calculate_daily_demand') as mock_calc:
        ...     mock_calc.return_value = 2.0
        ...     resultado = predict_stock_outage([1,2,3], 10)
        ...     resultado['estado'] == 'BAJO ⚠️'
        True
    """
    # Arrange
    historial_mock = [2, 2, 2]
    stock_actual = 4
    
    # Act
    with patch('services.prediction.stock_predictor.calculate_daily_demand') as mock_calc:
        mock_calc.return_value = 2.0  # Consumo de 2 unidades diarias
        resultado = predict_stock_outage(historial_mock, stock_actual)
        
    # Assert
    assert mock_calc.called
    assert resultado["dias_hasta_agotarse"] == 2.0
    assert resultado["estado"] == "CRÍTICO ⚠️"

def test_predict_stock_outage_empty_history():
    """Verifica que lance ValueError si el historial está vacío.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> predict_stock_outage([], 10) # Lanza ValueError
    """
    # Arrange
    historial_vacio = []
    stock_actual = 10
    
    # Act & Assert
    with pytest.raises(ValueError, match="El historial de ventas no puede estar vacío para predecir el stock"):
        predict_stock_outage(historial_vacio, stock_actual)
