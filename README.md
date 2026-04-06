# StockGuard - Sistema de Gestión de Inventarios

[![StockGuard CI](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml)

## Descripción

StockGuard es un sistema de gestión de existencias en Python 3.12. Este proyecto ha sido desarrollado como parte del Módulo 3 del curso, aplicando buenas prácticas de QA, documentación, tests y pipeline CI/CD.

El código original (`stockguard.py`) contenía vulnerabilidades críticas:
- Permitía cantidades y precios negativos.
- No manejaba archivos JSON corruptos.
- Carecía de tests y documentación.

En este repositorio se ha corregido todo, implementando:
- Modelo de datos con validación (`Item` dataclass).
- Módulo de validación (`validator.py`).
- Persistencia robusta (`storage.py`).
- Tests unitarios con pytest y mocks.
- Pipeline CI/CD con GitHub Actions (linting + tests automáticos).

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/kindred-98/StockGuard.git
   cd StockGuard