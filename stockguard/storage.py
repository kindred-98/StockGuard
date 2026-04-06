"""Módulo de persistencia para StockGuard.

Maneja la carga y guardado del inventario en un archivo JSON,
con tolerancia a errores de formato y archivo inexistente.
"""

import json
import os
from typing import List, Dict, Any

INVENTORY_FILE = 'inventory.json'


def load_inventory() -> List[Dict[str, Any]]:
    """Carga el inventario desde el archivo JSON.

    Si el archivo no existe, retorna una lista vacía.
    Si el archivo está corrupto (JSON mal formado), retorna una lista vacía.

    Returns:
        List[Dict[str, Any]]: Lista de ítems, cada uno con 'name', 'qty', 'price'.

    Example:
        >>> load_inventory()  # si no existe el archivo
        []
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Archivo corrupto: devolvemos lista vacía como fallback seguro
        return []
    except Exception:
        # Cualquier otro error (permisos, etc.) también devolvemos lista vacía
        return []


def save_inventory(items: List[Dict[str, Any]]) -> None:
    """Guarda el inventario en el archivo JSON con indentación.

    Args:
        items (List[Dict[str, Any]]): Lista de ítems a guardar.

    Example:
        >>> save_inventory([{'name': 'pera', 'qty': 5, 'price': 0.8}])
    """
    with open(INVENTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
