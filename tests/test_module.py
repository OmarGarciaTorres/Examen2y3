import pytest
from src.module import calculate_rectangle_area

def test_valid_rectangle_area():
    """Prueba con valores válidos de ancho y altura."""
    assert calculate_rectangle_area(5, 10) == 50

def test_zero_width():
    """Prueba cuando el ancho es cero."""
    with pytest.raises(ValueError):
        calculate_rectangle_area(0, 10)

def test_zero_height():
    """Prueba cuando la altura es cero."""
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, 0)

def test_negative_dimensions():
    """Prueba con dimensiones negativas."""
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, -10)

def test_large_values():
    """Prueba con valores grandes."""
    assert calculate_rectangle_area(1_000_000, 2_000_000) == 2_000_000_000_000
    
def test_invalid_types():
    """Prueba con tipos inválidos (no numéricos)."""
    with pytest.raises(TypeError):
        calculate_rectangle_area("a", "b")
