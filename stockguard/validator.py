"""Módulo de validación de datos para StockGuard.

Proporciona funciones para validar cantidad y precio de ítems.
"""


def validate_qty(qty: int) -> bool:
    """Valida que la cantidad sea un entero positivo.

    Args:
        qty (int): Cantidad a validar.

    Returns:
        bool: True si qty > 0, False en caso contrario.

    Raises:
        TypeError: Si qty no es un entero.

    Example:
        >>> validate_qty(10)
        True
        >>> validate_qty(0)
        False
        >>> validate_qty(-5)
        False
        >>> validate_qty(3.14)
        Traceback (most recent call last):
        ...
        TypeError: qty debe ser int, recibido <class 'float'>
    """
    if not isinstance(qty, int):
        raise TypeError(f"qty debe ser int, recibido {type(qty)}")
    return qty > 0


def validate_price(price: float) -> bool:
    """Valida que el precio sea un número positivo (float o int convertible).

    Args:
        price (float): Precio a validar. Se acepta int, pero se convierte a float.

    Returns:
        bool: True si price > 0, False en caso contrario.

    Raises:
        TypeError: Si price no es numérico (int o float).

    Example:
        >>> validate_price(10.5)
        True
        >>> validate_price(0)
        False
        >>> validate_price(-3.2)
        False
        >>> validate_price("10")
        Traceback (most recent call last):
        ...
        TypeError: price debe ser int o float, recibido <class 'str'>
    """
    if not isinstance(price, (int, float)):
        raise TypeError(f"price debe ser int o float, recibido {type(price)}")
    return float(price) > 0
