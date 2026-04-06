# stockguard.py --- código heredado (modificado para incluir validaciones)
import json
import os
from .validator import validate_qty, validate_price

INVENTORY_FILE = 'inventory.json'


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE) as f:
        return json.load(f)  # ⚠ sin manejo de JSON corrupto (se arreglará en storage.py)


def save_inventory(items):
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(items, f)


def add_item(name, qty, price):
    # Validaciones
    if not validate_qty(qty):
        raise ValueError(f"Cantidad inválida: {qty}. Debe ser entero positivo.")
    if not validate_price(price):
        raise ValueError(f"Precio inválido: {price}. Debe ser positivo.")

    items = load_inventory()
    items.append({'name': name, 'qty': qty, 'price': price})
    save_inventory(items)


def update_price(name, new_price):
    if not validate_price(new_price):
        raise ValueError(f"Precio inválido: {new_price}. Debe ser positivo.")

    items = load_inventory()
    for item in items:
        if item['name'] == name:
            item['price'] = new_price
            save_inventory(items)
            return
    # Opcional: lanzar error si no se encuentra el producto
    raise ValueError(f"Producto '{name}' no encontrado.")


def get_total_value():
    return sum(i['qty'] * i['price'] for i in load_inventory())
