# Pipeline CI/CD

Este documento registra los pasos implementados para configurar la Integración Continua (CI) del proyecto Inventario.

## Paso 1: Configuración de GitHub Actions (`ci.yml`)

Se ha creado el archivo `.github/workflows/ci.yml` correspondiente al **Commit 14**.

### Estructura del Pipeline

El flujo de trabajo se dispara automáticamente al hacer `push` o abrir un `pull_request` en las ramas principales.
Consta de un job principal llamado `test` apoyado en una estrategia de matrices.

### Matriz de Python

Garantiza que el código es estable y compatible a través de múltiples versiones modernas de Python. Se ejecuta simultáneamente en 4 entornos limpios de Ubuntu:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

### Secuencia de Pasos (Steps)

1. **Checkout:** Se utiliza `actions/checkout@v4` para clonar el repositorio dentro del contenedor de la Action.
2. **Setup Python:** Se inicializa el intérprete usando `actions/setup-python@v5` con la versión dictada por la matriz.
3. **Instalación de Dependencias:** Se actualiza `pip`, se instala el `requirements.txt` (si existe), y se instalan forzosamente las utilidades de testing (`pytest`, `pytest-mock`, `coverage`) y validación (`flake8`).
4. **Linting (flake8):** El linter analiza el código en busca de errores críticos (como variables sin definir o errores de sintaxis). En una segunda pasada, evalúa advertencias de estilo (líneas muy largas, alta complejidad ciclomática), pero se ha configurado con `--exit-zero` para que estas advertencias de estilo no hagan fracasar prematuramente el build durante la transición.
5. **Testing (pytest):** Finalmente, ejecuta `python -m pytest -v` para asegurar que el 100% de los tests unitarios y de integración de la Fase 4 resultan exitosos.

## Troubleshooting Registrado (Fixes)

### Error: `ModuleNotFoundError: No module named 'services'`

**Síntoma:** Al configurar el paso de tests con el comando base `pytest -v`, GitHub Actions falló devolviendo este error en todas las versiones de la matriz de Python.
**Causa:** GitHub Actions ejecuta el pipeline en un contenedor virgen. Por defecto, `pytest` por sí solo no añade siempre el directorio raíz (donde vive la carpeta `services/`) al `PYTHONPATH`, impidiendo que el motor localice los paquetes de código. En un entorno local, el IDE (o el propio comando en terminal local) suele inyectarlo.
**Solución:** Se cambió el comando en el archivo `.github/workflows/ci.yml` por `python -m pytest -v`. Al invocar pytest como un módulo de Python (`-m`), el intérprete automáticamente registra el directorio actual en el path del sistema, logrando localizar `services` sin errores.

# Captura pantalla Actions pipeline CI/CD

![Captura del pipeline en verde](images/captura_ci.png)
