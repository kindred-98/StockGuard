"""Tests para el módulo principal stockguard.py."""

import pytest
from unittest.mock import patch
from stockguard import stockguard


def test_add_item_valid():
    """add_item debe agregar un ítem válido al inventario."""
    test_data = [{"name": "manzana", "qty": 10, "price": 1.5}]

    with patch("stockguard.stockguard.load_inventory", return_value=test_data):
        with patch("stockguard.stockguard.save_inventory"):
            stockguard.add_item("naranja", 5, 2.0)
            stockguard.save_inventory.assert_called_once()


def test_add_item_invalid_qty_raises():
    """add_item debe lanzar ValueError si qty <= 0."""
    with pytest.raises(ValueError, match="Cantidad inválida"):
        stockguard.add_item("manzana", -5, 1.5)


def test_add_item_invalid_price_raises():
    """add_item debe lanzar ValueError si price <= 0."""
    with pytest.raises(ValueError, match="Precio inválido"):
        stockguard.add_item("manzana", 10, -1.0)


def test_update_price_valid():
    """update_price debe actualizar el precio de un ítem existente."""
    test_data = [{"name": "manzana", "qty": 10, "price": 1.5}]

    with patch("stockguard.stockguard.load_inventory", return_value=test_data):
        with patch("stockguard.stockguard.save_inventory"):
            stockguard.update_price("manzana", 2.0)
            stockguard.save_inventory.assert_called_once()


def test_update_price_not_found_raises():
    """update_price debe lanzar ValueError si el producto no existe."""
    test_data = [{"name": "manzana", "qty": 10, "price": 1.5}]

    with patch("stockguard.stockguard.load_inventory", return_value=test_data):
        with pytest.raises(ValueError, match="no encontrado"):
            stockguard.update_price("pera", 2.0)


def test_update_price_invalid_raises():
    """update_price debe lanzar ValueError si el nuevo precio es inválido."""
    with pytest.raises(ValueError, match="Precio inválido"):
        stockguard.update_price("manzana", -1.0)


def test_get_total_value():
    """get_total_value debe calcular el valor total del inventario."""
    test_data = [
        {"name": "manzana", "qty": 10, "price": 1.5},
        {"name": "naranja", "qty": 5, "price": 2.0},
    ]

    with patch("stockguard.stockguard.load_inventory", return_value=test_data):
        total = stockguard.get_total_value()
        assert total == 25.0


def test_get_total_value_empty_inventory():
    """get_total_value debe devolver 0 si el inventario está vacío."""
    with patch("stockguard.stockguard.load_inventory", return_value=[]):
        total = stockguard.get_total_value()
        assert total == 0
