"""Tests para el modelo Item de StockGuard."""

import pytest
from stockguard.models import Item


def test_item_creation_valid():
    """Test: crear un Item con valores válidos debe funcionar."""
    item = Item(name="Laptop", qty=10, price=999.99)
    assert item.name == "Laptop"
    assert item.qty == 10
    assert item.price == 999.99


def test_item_creation_minimal_positive():
    """Edge case: valores muy pequeños pero positivos deben ser aceptados."""
    item = Item(name="Clavo", qty=1, price=0.01)
    assert item.qty == 1
    assert item.price == 0.01


def test_item_creation_large_qty():
    """Edge case: cantidad muy grande (ej. 10^6) debe ser aceptada."""
    large_qty = 1_000_000
    item = Item(name="Tornillo", qty=large_qty, price=0.05)
    assert item.qty == large_qty


def test_item_qty_zero_raises_value_error():
    """qty=0 debe lanzar ValueError."""
    with pytest.raises(ValueError, match="La cantidad debe ser positiva"):
        Item(name="Ratón", qty=0, price=15.0)


def test_item_qty_negative_raises_value_error():
    """Qty negativo debe lanzar ValueError."""
    with pytest.raises(ValueError, match="La cantidad debe ser positiva"):
        Item(name="Teclado", qty=-5, price=25.0)


def test_item_price_zero_raises_value_error():
    """price=0 debe lanzar ValueError."""
    with pytest.raises(ValueError, match="El precio debe ser positivo"):
        Item(name="Monitor", qty=2, price=0.0)


def test_item_price_negative_raises_value_error():
    """Price negativo debe lanzar ValueError."""
    with pytest.raises(ValueError, match="El precio debe ser positivo"):
        Item(name="Tablet", qty=3, price=-10.5)


def test_item_price_very_small_positive():
    """Edge case: precio positivo muy pequeño (0.0001) debe ser válido."""
    item = Item(name="Microchip", qty=100, price=0.0001)
    assert item.price > 0


def test_item_qty_max_int():
    """Edge case: cantidad igual al máximo entero (2**31-1) debe ser válida."""
    max_int = 2**31 - 1
    item = Item(name="Cable", qty=max_int, price=1.99)
    assert item.qty == max_int
