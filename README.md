# StockGuard - Sistema de Gestión de Inventarios

[![StockGuard CI](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml)
[![Security Audit](https://github.com/kindred-98/StockGuard/actions/workflows/security.yml/badge.svg)](https://github.com/kindred-98/StockGuard/actions/workflows/security.yml)
[![Coverage](https://codecov.io/github/kindred-98/StockGuard/coverage.svg?branch=main)](https://codecov.io/github/kindred-98/StockGuard)

## Descripción

StockGuard es un sistema de gestión de existencias en Python 3.12+. Este proyecto ha sido desarrollado como parte del Módulo 3 del curso, aplicando buenas prácticas de QA, documentación, tests y pipeline CI/CD.

El código original (`stockguard.py`) contenía vulnerabilidades críticas:
- Permitía cantidades y precios negativos.
- No manejaba archivos JSON corruptos.
- Carecía de tests y documentación.

En este repositorio se ha corregido todo, implementando:
- Modelo de datos con validación (`Item` dataclass).
- Módulo de validación (`validator.py`).
- Persistencia robusta (`storage.py`).
- Tests unitarios con pytest y mocks (34 tests, 89% coverage).
- Pipeline CI/CD con GitHub Actions (linting + tests + coverage).
- Pipeline de seguridad con Bandit.
- Pre-commit hooks con flake8 y black.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/kindred-98/StockGuard.git
   cd StockGuard
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Instala pre-commit hooks (opcional):
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Uso

### Ejecutar tests

```bash
pytest tests/ -v
```

### Ejecutar tests con coverage

```bash
pytest tests/ --cov=stockguard --cov-report=term-missing
```

### Ejecutar linting

```bash
flake8 stockguard/ tests/ --max-line-length=100
```

### Escaneo de seguridad

```bash
bandit -r stockguard/
```

## Pipelines

| Pipeline | Descripción | Trigger |
|----------|-------------|---------|
| CI | Lint + Tests + Coverage | push/PR a main |
| Security | Bandit security scan | push/PR a main |

## Estructura del Proyecto

```
stockguard/
├── stockguard/
│   ├── __init__.py
│   ├── stockguard.py    # Código original (con validaciones)
│   ├── models.py        # Dataclass Item
│   ├── validator.py     # Validaciones de entrada
│   └── storage.py      # Persistencia JSON
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_validator.py
│   ├── test_storage.py
│   └── test_stockguard.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── security.yml
├── .pre-commit-config.yaml
├── requirements.txt
├── README.md
└── AUDIT.md
```

## Uso de IA

Durante el desarrollo se utilizó IA para:
- Generación de esqueletos de docstrings (estilo Google).
- Casos base de tests unitarios.
- Configuración inicial del pipeline CI/CD.

**Nota**: Todo el código generado por IA fue revisado, entendido y adaptado antes de ser incorporado al proyecto.

## Badges

Los badges se generan automáticamente en GitHub Actions:
- Configurar en **Settings > Actions > General > Workflow run permissions**
- Para coverage: configurar **Settings > Codecov**
