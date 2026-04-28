from services.vision.detector import detect_products
from unittest.mock import patch

def test_detect_products_mocked():
    """Verifica la detección simulada usando un mock para la elección aleatoria.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> with patch('services.vision.detector.random.choice') as mock_choice:
        ...     mock_choice.return_value = {"descripcion": "Test", "productos": [{"nombre": "Pan", "cantidad": 5, "confianza": 0.9}]}
        ...     resultado = detect_products()
        ...     'productos' in resultado
        True
    """
    # Arrange
    mock_scenario = {
        "descripcion": "Escenario Mockeado",
        "productos": [
            {"nombre": "Leche", "cantidad": 10, "confianza": 0.99}
        ]
    }

    # Act
    with patch('services.vision.detector.random.choice') as mock_choice:
        mock_choice.return_value = mock_scenario
        resultado = detect_products("dummy_path.jpg")

    # Assert
    assert mock_choice.called
    assert "productos" in resultado
    assert len(resultado["productos"]) > 0
    assert resultado["descripcion"] == "Escenario Mockeado"
