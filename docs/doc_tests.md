# Documentación de Tests (doc_tests.md)

Este documento describe los tests implementados en el proyecto.

## Capa de Base de Datos (`tests/database/`)

### `test_product_db.py`
- Verifica que existan exactamente los 25 productos.
- Verifica que todas las categorías sean válidas.
- Verifica que cada producto contenga todos los campos obligatorios del esquema.

### `test_db_reader.py`
- Verifica la búsqueda de información de un producto existente e inexistente.
- Valida que `get_all_products()` retorne la lista íntegra de 25 productos.

### `test_db_filter.py`
- Valida que `get_sales_history()` devuelva datos correctos o listas vacías en caso de fallos.
- Verifica el correcto filtrado por categorías, incluyendo *case-insensitivity*.

## Capa de Visión (`tests/vision/`)

### `test_scenario_loader.py`
- **`test_load_scenarios_structure`**: Verifica que la función devuelva una lista de escenarios, cada uno con una `descripcion` y una lista de `productos`. Se valida además que los productos contengan las claves `nombre`, `cantidad` y `confianza`.

### `test_detector.py`
- **`test_detect_products_mocked`**: Comprueba el funcionamiento de la orquestación. Usa un *mock* (`unittest.mock.patch`) en `random.choice` para inyectar un escenario controlado y asegurar que el sistema procesa correctamente diccionarios con la clave `productos` y que las listas no vengan vacías.

## Capa de Inventario (`tests/inventory/`)

### `test_metrics.py`
- Verifica el conteo exacto de productos en estado CRÍTICO, BAJO y ADECUADO, validando su correspondencia con la base de datos real.
- Asegura que al proveer una lista vacía, el sistema devuelva de forma segura todos los contadores a `0`.

### `test_valuation.py`
- Valida que el sumatorio del inventario sea correcto matemáticamente (`precio x stock`).
- Comprueba que los productos enviados por visión que no existen en la BD devuelvan un valor de `0` sin lanzar excepciones.
- Asegura que procesar una lista de visión vacía devuelva `0.0`.

### `test_recommender.py`
- Verifica que el sistema etiquete como prioridad `ALTA` (Urgente) a un producto si su stock enviado es igual a `0`.
- Verifica que devuelva prioridad `MEDIA` si el stock es inferior al mínimo pero mayor que `0`.

## Capa de Predicción (`tests/prediction/`)

### `test_demand_analyzer.py`
- Verifica el cálculo de consumo promedio con listas válidas de historial.
- Comprueba que un historial de un único elemento no rompa el cálculo.
- Asegura que al proveer una lista vacía, se propague el correspondiente `ValueError` por falta de datos.

### `test_stock_predictor.py`
- **`test_predict_stock_outage_mock_demand`**: Valida que el clasificador de estado por rangos de días funcione. Utiliza `unittest.mock.patch` en la función `calculate_daily_demand` para simular un consumo fijo (2 unidades) y predecir correctamente cuántos días faltan para agotarse y qué estado asignar.
- Verifica que pasar una lista vacía para un producto con stock levante un `ValueError`.

## Integración (`tests/integration/`)

### `test_full_pipeline.py`
- Ejecuta una prueba de tipo End-to-End (`e2e`). 
- Flujo: Arranca un escaneo desde la capa de visión (`detect_products`), cruza con la base de datos para recuperar históricos, analiza y predice posibles cortes de inventario (`predict_stock_outage`), y por último, inyecta las deficiencias al motor de recomendación (`generate_recommendations`).
- Garantiza estructuralmente que un cambio aislado en uno de los micro-servicios no rompa la estructura de datos que recibe el subsiguiente.
