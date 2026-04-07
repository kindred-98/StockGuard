"""StockGuard - Código heredado con validaciones.

Módulo principal del sistema de gestión de inventarios.
Contiene las funciones de negocio para gestionar items.
"""

import json
import os
from .validator import validate_qty, validate_price

INVENTORY_FILE = "inventory.json"


def load_inventory():
    """Carga el inventario desde el archivo JSON.

    Returns:
        list: Lista de diccionarios con items del inventario.
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_inventory(items):
    """Guarda el inventario en el archivo JSON.

    Args:
        items (list): Lista de diccionarios con items.
    """
    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f)


def add_item(name, qty, price):
    """Añade un nuevo item al inventario.

    Args:
        name (str): Nombre del producto.
        qty (int): Cantidad del producto.
        price (float): Precio del producto.

    Raises:
        ValueError: Si la cantidad o precio no son válidos.
    """
    if not validate_qty(qty):
        raise ValueError(f"Cantidad inválida: {qty}. Debe ser entero positivo.")
    if not validate_price(price):
        raise ValueError(f"Precio inválido: {price}. Debe ser positivo.")

    items = load_inventory()
    items.append({"name": name, "qty": qty, "price": price})
    save_inventory(items)


def update_price(name, new_price):
    """Actualiza el precio de un producto existente.

    Args:
        name (str): Nombre del producto.
        new_price (float): Nuevo precio del producto.

    Raises:
        ValueError: Si el precio no es válido o el producto no existe.
    """
    if not validate_price(new_price):
        raise ValueError(f"Precio inválido: {new_price}. Debe ser positivo.")

    items = load_inventory()
    for item in items:
        if item["name"] == name:
            item["price"] = new_price
            save_inventory(items)
            return
    raise ValueError(f"Producto '{name}' no encontrado.")


def get_total_value():
    """Calcula el valor total del inventario.

    Returns:
        float: Suma de (cantidad * precio) de todos los items.
    """
    return sum(i["qty"] * i["price"] for i in load_inventory())
