<div align="center">

# StockGuard

### Sistema de Gestión de Inventarios - Python 3.12+

[![StockGuard CI](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/kindred-98/StockGuard/actions/workflows/ci.yml)
[![Security Audit](https://github.com/kindred-98/StockGuard/actions/workflows/security.yml/badge.svg)](https://github.com/kindred-98/StockGuard/actions/workflows/security.yml)
[![Coverage](https://codecov.io/gh/kindred-98/StockGuard/branch/main/graph/badge.svg)](https://codecov.io/gh/kindred-98/StockGuard)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=kindred-98_StockGuard&metric=alert_status)](https://sonarcloud.io/dashboard?id=kindred-98_StockGuard)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📋 Descripción del Proyecto

StockGuard es un sistema de gestión de inventarios desarrollado en Python 3.12+, diseñado siguiendo los más altos estándares de calidad de software. El proyecto surge como ejercicio académico del Módulo 3, pero ha evolucionado hasta convertirse en un referente de buenas prácticas en QA, documentación y CI/CD.

### Origen del Proyecto

El código inicial, proporcionado como "legacy code", contenía vulnerabilidades críticas que fueron identificadas, documentadas y corregidas sistemáticamente. Este proceso de auditoría y mejora continua es exactamente el tipo de disciplina que distingue a un profesional QA senior.

### Estado Actual

| Métrica | Valor | Estado |
|---------|-------|--------|
| Tests | 34 | ✅ |
| Coverage | 97% | ✅ |
| Quality Gate | Passed | ✅ |
| Security Issues | 0 | ✅ |
| Code Smells | 0 | ✅ |

---

## 🏗️ Arquitectura del Sistema

```
StockGuard/
├── .github/workflows/      # Pipelines CI/CD
│   ├── ci.yml            # Pipeline principal
│   └── security.yml      # Pipeline de seguridad
├── stockguard/           # Código fuente
│   ├── models.py         # Modelo de datos
│   ├── validator.py      # Validaciones de negocio
│   ├── storage.py        # Capa de persistencia
│   └── stockguard.py     # Lógica de negocio
├── tests/                # Suite de tests
├── docs/                 # Documentación técnica
└── sonar-project.properties
```

---

## 🔍 Análisis de Calidad

### Pilares de Calidad implementados

1. **Validación de Datos**: Sistema robusto de validación en múltiples capas
2. **Manejo de Errores**: Tolerancia a fallos en operaciones de E/S
3. **Test Coverage**: Cobertura casi total del código de negocio
4. **Documentación**: Docstrings en formato Google en todas las funciones públicas
5. **Seguridad**: Validación de entradas para prevenir inyección de datos maliciosos
6. **Integración Continua**: 3 pipelines automatizados trabajando en synergy

### Vulnerabilidades Corregidas

El código original presentaba las siguientes vulnerabilidades críticas:

| # | Vulnerabilidad | Impacto | Solución Implementada |
|---|----------------|---------|---------------------|
| 1 | Entrada sin validación | Stock y precios negativos | `validator.py` con `__post_init__` |
| 2 | JSON corrupto | Crasheo del sistema | Manejo de excepciones en `storage.py` |
| 3 | Sin tests | Imposible verificar funcionamiento | 34 tests unitarios con mocks |
| 4 | Sin documentación | Mantenimiento imposible | Docstrings Google + README |
| 5 | Dependencias vulnerables en librerías de terceros | Riesgo de ejecución o escalada por paquetes externos | `requirements.txt` actualizado y documentación en `docs/SNYK_Vulnerabilidades.md` |

---

## 🔒 Pipelines de Calidad

Este proyecto implementa una estrategia de **Defense in Depth** con tres líneas de defensa automatizadas:

### Pipeline 1: CI (Continuous Integration)

```
Trigger: Push o PR a main
```

| Etapa | Herramienta | Propósito |
|-------|-------------|-----------|
| Linting | flake8 | Verificar estilo PEP 8 |
| Testing | pytest | Ejecutar tests unitarios |
| Coverage | pytest-cov | Medir cobertura de código |
| Analysis | SonarCloud | Análisis estático de calidad |

### Pipeline 2: Security

```
Trigger: Push o PR a main
```

| Etapa | Herramienta | Propósito |
|-------|-------------|-----------|
| Scanning | Bandit | Detectar vulnerabilidades de seguridad |
| Report | artifact | Disponibilizar reporte |

### Pipeline 3: Pre-commit (Local)

```
Trigger: Antes de cada commit
```

| Herramienta | Propósito |
|-------------|-----------|
| flake8 | Linting automático |
| black | Formateo de código |

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.12 o superior
- Git
- Cuenta en GitHub (para pipelines)
- Cuenta en SonarCloud (opcional, para métricas)

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/kindred-98/StockGuard.git
cd StockGuard

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. (Opcional) Instalar pre-commit hooks
pip install pre-commit
pre-commit install
```

---

## ⚡ Uso del Sistema

### Ejecutar Tests

```bash
# Tests básicos
pytest tests/ -v

# Tests con coverage
pytest tests/ --cov=stockguard --cov-report=term-missing

# Tests en paralelo (más rápido)
pytest tests/ -n auto

# Tests con salida detallada
pytest tests/ -v --tb=short
```

### Ejecutar Linting

```bash
# Flake8
flake8 stockguard/ tests/ --max-line-length=100

# Black (formateo)
black stockguard/ tests/

# pylint
pylint stockguard/

# mypy (tipado estático)
mypy stockguard/
```

### Escaneo de Seguridad

```bash
# Bandit
bandit -r stockguard/

# Safety (dependencias)
safety check
```

---

## 📊 Métricas de Calidad

### Coverage por Módulo

| Módulo | Cobertura |
|--------|-----------|
| `models.py` | 86% |
| `storage.py` | 100% |
| `validator.py` | 100% |
| `stockguard.py` | 81% |
| **TOTAL** | **97%** |

### Distribución de Tests

| Categoría | Cantidad |
|-----------|----------|
| Tests de modelos | 9 |
| Tests de validación | 10 |
| Tests de almacenamiento | 6 |
| Tests de integración | 8 |
| Tests de seguridad | 1 |

---

## 🛠️ Configuración de Herramientas

### Variables de Entorno

No se requieren variables de entorno para el funcionamiento básico.

### Secrets de GitHub

| Secret | Descripción | Obligatorio |
|--------|-------------|-------------|
| `SONAR_TOKEN` | Token de SonarCloud | No (solo métricas) |

### Configuración de Pipelines

#### SonarCloud

El proyecto está configurado para análisis con SonarCloud. Para activar:
1. Crear cuenta en sonarcloud.io
2. Importar el repositorio
3. Generar token en My Account → Security
4. Añadir secret `SONAR_TOKEN` en GitHub

---

## 📚 Documentación Adicional

| Documento | Descripción |
|-----------|-------------|
| [README](README.md) | Guía de uso rápido |
| [Auditoria.md](docs/Auditoria.md) | Auditoría de vulnerabilidades |
| [PIPELINES_EXPLICACION.md](docs/PIPELINES_EXPLICACION.md) | Detalle de pipelines |
| [Inf_Completo-Desarrollo.md](docs/Inf_Completo-Desarrollo.md) | Informe completo de desarrollo |

---

## 🤝 Contribución

Este proyecto es de carácter académico, pero las contribuciones son bienvenidas.

### Guidelines

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/NuevaFeature`)
3. Commit con mensajes convencionales
4. Push y crear Pull Request
5. Asegurar que CI pase en verde

### Estándares de Código

- **PEP 8** para estilo
- **Google Docstrings** para documentación
- **Type hints** para tipado estático
- **100 caracteres** por línea máximo

---

## 📝 Reflection A.D.E.V

> *Después dos dias como QA, he aprendido que la diferencia entre un código "que funciona" y código de "calidad profesional" está en la disciplina. Este proyecto demuestra que incluso un ejercicio académico puede convertirse en un caso de estudio de excellence en ingeniería de software.*
>
> *Las lecciones clave:*
> - *La validación nunca es excesiva*
> - *Los tests son documentación executable*
> - *La automatización es tu mejor aliada*
> - *La seguridad no es una opción, es una obligación*

---

## 📜 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

---

## 🔗 Enlaces Útiles

- [Repositorio GitHub](https://github.com/kindred-98/StockGuard)
- [SonarCloud Dashboard](https://sonarcloud.io/dashboard?id=kindred-98_StockGuard)
- [GitHub Actions](https://github.com/kindred-98/StockGuard/actions)
- [Documentación Python](https://docs.python.org/3/)

---

*Última actualización: Abril 2026*
