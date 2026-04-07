# Pipelines de StockGuard - Documentación

## Resumen de Pipelines

Este proyecto cuenta con **3 pipelines automatizados** en GitHub Actions que trabajan juntos para garantizar la calidad y seguridad del código.

```
┌─────────────────────────────────────────────────────────────────┐
│                    GITHUB ACTIONS                              │
├─────────────────┬─────────────────┬───────────────────────────┤
│      CI         │    SECURITY     │     SONARCLOUD           │
│  (ci.yml)       │ (security.yml)  │    (integrado en CI)     │
├─────────────────┼─────────────────┼───────────────────────────┤
│ • flake8        │ • Bandit        │ • Análisis estático      │
│ • pytest        │ • Escaneo       │ • Métricas de calidad    │
│ • coverage      │   de seguridad │ • Debt técnico           │
└─────────────────┴─────────────────┴───────────────────────────┘
```

---

## Pipeline 1: CI (Continuous Integration)

**Archivo:** `.github/workflows/ci.yml`

### ¿Qué hace?
Ejecuta verificaciones de **calidad del código** en cada push o PR a `main`.

### Pasos:
1. **Checkout** - Descarga el código
2. **Setup Python 3.12** - Configura el entorno
3. **Install dependencies** - Instala pytest, flake8, coverage
4. **Lint with flake8** - Verifica estilo de código (líneas max 100)
5. **Run tests with pytest** - Ejecuta 34 tests unitarios
6. **Coverage** - Genera reporte de cobertura (objetivo ≥80%)
7. **SonarCloud Scan** - Análisis de calidad (bugs, code smells, debt)

### Cuándo se ejecuta:
- Push a `main`
- Pull Request a `main`

### Resultado esperado:
- ✅ Verde = Código pasa todas las verificaciones
- ❌ Rojo = Alguna verificación falló

---

## Pipeline 2: Security (Auditoría de Seguridad)

**Archivo:** `.github/workflows/security.yml`

### ¿Qué hace?
Ejecuta **Bandit** para detectar vulnerabilidades de seguridad en el código Python.

### Pasos:
1. **Checkout** - Descarga el código
2. **Setup Python 3.12** - Configura el entorno
3. **Install Bandit** - Instala la herramienta de seguridad
4. **Run Bandit** - Escanea `stockguard/` en busca de:
   - Inyecciones de código
   - Contraseñas hardcodeadas
   - Uso de funciones peligrosas
   - Cryptography issues
5. **Upload Report** - Guarda el reporte como artefacto

### Cuándo se ejecuta:
- Push a `main`
- Pull Request a `main`

### Resultado esperado:
- Reporte `bandit_report.txt` disponible para descargar

---

## Pipeline 3: SonarCloud (Análisis de Calidad)

**Archivo:** Integrado en `ci.yml`

### ¿Qué hace?
Analiza el código para detectar:
- **Bugs** - Errores potenciales
- **Code Smells** - Código difícil de mantener
- **Security Hotspots** - Zonas sensibles a seguridad
- **Technical Debt** - Deuda técnica acumulada
- **Coverage** - Cobertura de tests
- **Duplications** - Código duplicado

### Cómo se integra:
El análisis se ejecuta automáticamente dentro del pipeline CI después de los tests.

### Requisitos:
- Token de SonarCloud configurado en GitHub Secrets (`SONAR_TOKEN`)
- Automatic Analysis desactivado en SonarCloud (Administration → Analysis Method)

---

## Cómo interactúan entre ellos

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   PUSH       │────▶│    CI        │────▶│   SONARCLOUD │
│   / PR       │     │  (Calidad)   │     │  (Análisis)  │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │   SECURITY   │
                    │  (Bandit)    │
                    └──────────────┘
```

1. **Cuando haces push o PR**: Se activan todos los pipelines
2. **CI** verifica que el código funcione y cumpla el estilo
3. **Security** busca vulnerabilidades de seguridad
4. **SonarCloud** analiza la calidad técnica

**Todos deben pasar en verde** para considerar el código listo.

---

## Para qué sirve este código

### ¿Por qué tener 3 pipelines?

| Pipeline | Propósito | Beneficio |
|----------|-----------|-----------|
| **CI** | Verificar que el código funciona | No romper la aplicación |
| **Security** | Detectar vulnerabilidades | Proteger contra ataques |
| **SonarCloud** | Mejorar calidad técnica | Código mantenible a largo plazo |

### ¿Qué problemas detectan?

- **CI**: Tests fallan, estilo incorrecto, coverage bajo
- **Security**: Contraseñas en código, funciones peligrosas, inyecciones
- **SonarCloud**: Bugs potenciales, código duplicado, deuda técnica

---

## Cómo usarlos

### 1. Ejecutar localmente antes de push

```bash
# Verificar tests
pytest tests/ -v

# Verificar coverage
pytest tests/ --cov=stockguard --cov-report=term-missing

# Verificar estilo
flake8 stockguard/ tests/ --max-line-length=100

# Verificar seguridad
bandit -r stockguard/
```

### 2. Hacer un push

```bash
git add .
git commit -m "tu mensaje"
git push origin main
```

### 3. Ver resultados

1. **GitHub Actions**: Ve a tu repo → Actions
2. **SonarCloud**: Ve a sonarcloud.io → tu proyecto
3. **Security Report**: En el artifact del pipeline Security

### 4. Configurar SonarCloud (primera vez)

1. Ve a **sonarcloud.io**
2. Importa tu repositorio `StockGuard`
3. Genera un token en **My Account → Security**
4. Añádelo en GitHub: **Settings → Secrets → SONAR_TOKEN**

---

## Badges disponibles

En el README.md tienes badges que muestran el estado:

```markdown
[![StockGuard CI](https://github.com/TU-USUARIO/StockGuard/actions/workflows/ci.yml/badge.svg)](URL)
[![Security Audit](https://github.com/TU-USUARIO/StockGuard/actions/workflows/security.yml/badge.svg)(URL)
[![Coverage](https://codecov.io/github/TU-USUARIO/StockGuard/coverage.svg?branch=main)](URL)
```

---

## Tabla resumen

| Pipeline | Archivo | Herramienta | Frecuencia | Obligatorio |
|----------|---------|-------------|------------|-------------|
| CI | ci.yml | flake8 + pytest | Push/PR | ✅ |
| Security | security.yml | Bandit | Push/PR | ✅ |
| SonarCloud | ci.yml | SonarScanner | Push/PR | ✅ (con token) |

---

## Troubleshooting

### Si CI falla:
- Revisa el log de flake8 (errores de estilo)
- Revisa el log de pytest (tests fallando)

### Si Security falla:
- Revisa `bandit_report.txt` en los artefactos
- Corrige las vulnerabilidades marcadas

### Si SonarCloud falla:
- Verifica que `SONAR_TOKEN` esté configurado
- Desactiva Automatic Analysis en SonarCloud
- Revisa las métricas en sonarcloud.io
