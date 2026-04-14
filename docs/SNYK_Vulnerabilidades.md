# Auditoría de seguridad Snyk

## Resumen

Este documento recoge las vulnerabilidades identificadas por Snyk en el proyecto StockGuard y las acciones tomadas para mitigarlas.

- Fecha del escaneo: 14 de abril de 2026
- Herramienta: Snyk
- Vulnerabilidades abiertas detectadas: 9
- Estado actual: mitigadas mediante actualización de dependencias y fijado de versiones seguras

## Dependencias afectadas y mitigación

| Dependencia | Versiones vulnerables detectadas | Versión segura recomendada | Acción aplicada |
|-------------|----------------------------------|----------------------------|-----------------|
| `setuptools` | 40.5.0 | 78.1.1 | Actualizado en `requirements.txt` a `setuptools>=78.1.1` |
| `zipp` | 3.15.0 | 3.19.1 | Actualizado en `requirements.txt` a `zipp>=3.19.1` |
| `urllib3` | 2.0.7 | 2.2.2 | Actualizado en `requirements.txt` a `urllib3>=2.2.2` |
| `requests` | indirecta | 2.32.2 | Fijado en `requirements.txt` a `requests>=2.32.2` |
| `cryptography` | indirecta | 46.0.5 | Fijado en `requirements.txt` a `cryptography>=46.0.5` |
| `authlib` | indirecta | 1.3.1 | Fijado en `requirements.txt` a `authlib>=1.3.1` |
| `marshmallow` | indirecta | 3.26.2 | Fijado en `requirements.txt` a `marshmallow>=3.26.2` |
| `filelock` | indirecta | 3.20.1 | Fijado en `requirements.txt` a `filelock>=3.20.1` |

> Nota: varias de estas dependencias no son usadas directamente por el código del proyecto, pero se fijan en `requirements.txt` para garantizar que el entorno de desarrollo y CI use versiones seguras.

## Resultados

- Las vulnerabilidades referidas por Snyk pertenecen a dependencias del entorno y no al código fuente de StockGuard.
- El archivo `requirements.txt` ya contiene las versiones mínimas seguras necesarias para mitigar los problemas detectados.
- Se recomienda ejecutar los siguientes pasos después de actualizar dependencias:
  1. `python -m pip install --upgrade pip`
  2. `python -m pip install -r requirements.txt`
  3. `pytest`
  4. `python -m bandit -r stockguard/`
  5. Realizar un nuevo escaneo Snyk para verificar la corrección completa.

## Seguimiento

- Archivo de configuración de dependencias seguro: `requirements.txt`
- Documentación de la auditoría: `docs/SNYK_Vulnerabilidades.md`
- Informe de seguridad general: `docs/Auditoria.md`
