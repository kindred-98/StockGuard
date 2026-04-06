"""Modelo de datos para StockGuard.

Define la estructura de un ítem de inventario con validación en la creación.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Item:
    """Representa un producto en el inventario.

    Attributes:
        name (str): Nombre del producto.
        qty (int): Cantidad disponible (debe ser > 0).
        price (float): Precio unitario (debe ser > 0).

    Raises:
        ValueError: Si qty <= 0 o price <= 0.
        TypeError: Si los tipos no coinciden (por conversión automática de dataclass).
    """

    name: str
    qty: int
    price: float

    def __post_init__(self) -> None:
        """Valida que la cantidad y el precio sean positivos después de la inicialización.

        Raises:
            ValueError: Si qty <= 0 o price <= 0.
        """
        if self.qty <= 0:
            raise ValueError(f"La cantidad debe ser positiva, recibido: {self.qty}")
        if self.price <= 0:
            raise ValueError(f"El precio debe ser positivo, recibido: {self.price}")

    # Opcional: método para convertir a diccionario (compatible con storage)
    def to_dict(self) -> dict[str, Any]:
        """Convierte el Item a diccionario para guardar en JSON.

        Returns:
            dict: Con claves 'name', 'qty', 'price'.
        """
        return {"name": self.name, "qty": self.qty, "price": self.price}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Item":
        """Crea un Item desde un diccionario (cargado de JSON).

        Args:
            data (dict): Diccionario con claves 'name', 'qty', 'price'.

        Returns:
            Item: Instancia válida (puede lanzar ValueError si datos inválidos).
        """
        return cls(name=data["name"], qty=data["qty"], price=data["price"])