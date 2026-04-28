from services.vision.scenario_loader import _load_scenarios

def test_load_scenarios_structure():
    """Verifica que la estructura de los escenarios sea correcta.

    Args: Ninguno.
    Returns: None.
    Example:
        >>> escenarios = _load_scenarios()
        >>> 'productos' in escenarios[0]
        True
    """
    # Arrange
    # (No se requiere configuración previa para este test)

    # Act
    escenarios = _load_scenarios()

    # Assert
    assert isinstance(escenarios, list)
    assert len(escenarios) > 0
    for escenario in escenarios:
        assert "descripcion" in escenario
        assert "productos" in escenario
        productos = escenario["productos"]
        assert isinstance(productos, list)
        for p in productos:
            assert "nombre" in p
            assert "cantidad" in p
            assert "confianza" in p
