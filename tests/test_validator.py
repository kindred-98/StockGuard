"""Tests para las funciones de validación de StockGuard."""

import pytest
from stockguard.validator import validate_qty, validate_price


def test_validate_qty_valid():
    """validate_qty debe devolver True para enteros positivos."""
    assert validate_qty(5) is True
    assert validate_qty(1) is True
    assert validate_qty(1000) is True


def test_validate_qty_zero():
    """validate_qty debe devolver False para qty = 0."""
    assert validate_qty(0) is False


def test_validate_qty_negative():
    """validate_qty debe devolver False para qty negativo."""
    assert validate_qty(-1) is False
    assert validate_qty(-100) is False


def test_validate_qty_raises_type_error_on_non_int():
    """validate_qty debe lanzar TypeError si qty no es entero."""
    with pytest.raises(TypeError, match="qty debe ser int"):
        validate_qty(3.14)
    with pytest.raises(TypeError, match="qty debe ser int"):
        validate_qty("10")
    with pytest.raises(TypeError, match="qty debe ser int"):
        validate_qty(None)


def test_validate_qty_edge_case_large_int():
    """Edge case: cantidad muy grande (2**63-1) debe ser True."""
    huge_qty = 2**63 - 1
    assert validate_qty(huge_qty) is True


def test_validate_price_valid():
    """validate_price debe devolver True para precios positivos."""
    assert validate_price(10.5) is True
    assert validate_price(0.01) is True
    assert validate_price(1000.0) is True
    # También debe aceptar ints
    assert validate_price(42) is True


def test_validate_price_zero():
    """validate_price debe devolver False para price = 0."""
    assert validate_price(0) is False
    assert validate_price(0.0) is False


def test_validate_price_negative():
    """validate_price debe devolver False para price negativo."""
    assert validate_price(-5.5) is False
    assert validate_price(-1) is False


def test_validate_price_raises_type_error_on_non_numeric():
    """validate_price debe lanzar TypeError si price no es numérico."""
    with pytest.raises(TypeError, match="price debe ser int o float"):
        validate_price("10.5")
    with pytest.raises(TypeError, match="price debe ser int o float"):
        validate_price([1, 2])
    with pytest.raises(TypeError, match="price debe ser int o float"):
        validate_price(None)


def test_validate_price_edge_case_very_small_positive():
    """Edge case: precio positivo muy pequeño (1e-10) debe ser True."""
    tiny_price = 1e-10
    assert validate_price(tiny_price) is True


def test_validate_price_edge_case_very_large_float():
    """Edge case: precio enorme (1e15) debe ser True."""
    huge_price = 1e15
    assert validate_price(huge_price) is True
