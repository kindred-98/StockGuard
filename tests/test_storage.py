"""Tests para el módulo de persistencia storage.py usando mocks."""

import json
import pytest
from unittest.mock import mock_open, patch
from stockguard import storage

# ----------------------------------------------------------------------
# Tests para load_inventory
# ----------------------------------------------------------------------

def test_load_inventory_file_not_found():
    """Cuando el archivo no existe, load_inventory debe devolver lista vacía."""
    with patch('stockguard.storage.os.path.exists', return_value=False):
        result = storage.load_inventory()
        assert result == []

def test_load_inventory_valid_json():
    """Cuando el archivo existe y es JSON válido, debe devolver los datos."""
    mock_data = [{"name": "manzana", "qty": 10, "price": 1.5}]
    mock_json = json.dumps(mock_data)
    
    with patch('stockguard.storage.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_json)):
            result = storage.load_inventory()
            assert result == mock_data

def test_load_inventory_corrupt_json():
    """Cuando el archivo existe pero el JSON está corrupto, debe devolver lista vacía."""
    corrupt_json = '{"name": "manzana", "qty": 10, "price": 1.5'  # JSON incompleto
    
    with patch('stockguard.storage.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=corrupt_json)):
            result = storage.load_inventory()
            assert result == []

def test_load_inventory_exception_handling():
    """Cualquier otra excepción (ej. permisos) también debe devolver lista vacía."""
    with patch('stockguard.storage.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open()) as mock_file:
            # Simular una excepción genérica al hacer json.load
            mock_file.side_effect = Exception("Error de permisos")
            result = storage.load_inventory()
            assert result == []

# ----------------------------------------------------------------------
# Tests para save_inventory
# ----------------------------------------------------------------------

def test_save_inventory_with_indent():
    """save_inventory debe guardar el JSON con indent=2."""
    items = [{"name": "pera", "qty": 5, "price": 0.8}]
    expected_json = json.dumps(items, indent=2, ensure_ascii=False)
    
    with patch('builtins.open', mock_open()) as mocked_file:
        storage.save_inventory(items)
        # Verificar que se llamó a open con 'w'
        mocked_file.assert_called_once_with(storage.INVENTORY_FILE, 'w', encoding='utf-8')
        # Obtener el argumento con el que se llamó a write
        handle = mocked_file()
        # El contenido escrito debe ser el JSON con indentación
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        assert written_data == expected_json

def test_save_inventory_empty_list():
    """Guardar una lista vacía debe producir un JSON con '[]' e indentación."""
    items = []
    expected_json = json.dumps(items, indent=2, ensure_ascii=False)
    
    with patch('builtins.open', mock_open()) as mocked_file:
        storage.save_inventory(items)
        handle = mocked_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        assert written_data == expected_json