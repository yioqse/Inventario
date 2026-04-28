FASE 4 — Tests unitarios

# Commit Qué debe contener Tarea

09 test: tests de database/ [ai] ✅ [COMPLETADO]
test_product_db.py, test_db_reader.py, test_db_filter.py.
Cubrir valores válidos, inválidos, lista vacía, filtro por
categoría
Alumno/a
10 test: tests de vision/ [ai] ✅ [COMPLETADO]
test_detector.py, test_scenario_loader.py. Mock de
random.choice(). Verificar estructura del escenario. Edge
case: lista vacía
Alumno/a
11 test: tests de inventory/ [ai] ✅ [COMPLETADO]
test_metrics.py, test_valuation.py, test_recommender.py.
Cubrir estado crítico, bajo, normal. Lista vacía. Producto no
encontrado en BD
Alumno/a
12 test: tests de prediction/ [ai] ✅ [COMPLETADO]
test_demand_analyzer.py, test_stock_predictor.py.
pytest-mock para historial de ventas. Verificar ValueError con
historial vacío
Alumno/a
13 test: test_full_pipeline.py —
integración [ai]
Test de integración end-to-end: detect_products → predict →
recommend. Verifica que la cadena completa no lanza
excepciones
Alumno/a

cov run --source=services -m pytest tests/integration/test_full_pipeline.py

BLOQUE 5 — Tests Unitarios con pytest
La suite de tests refleja la estructura SRP del código: cada archivo de test cubre exactamente un módulo.
Los tests deben seguir la convención AAA (Arrange-Act-Assert) y tener docstring Google en cada función
de test.
5.1 — Mapa de cobertura requerida
Archivo de test Módulo que cubre Casos mínimos requeridos
test_product_db.py product_db.py 25 productos presentes, categorías
correctas, tipos de datos
test_db_reader.py db_reader.py get_product_info() válido, inválido, None
test_db_filter.py db_filter.py
get_by_category() con categoría
existente, inexistente, vacía
test_scenario_loader.py scenario_loader.py
Escenarios tienen lista 'productos', cada
producto tiene 'nombre' y 'cantidad'
test_detector.py detector.py
Mock de random.choice(). Resultado
tiene clave 'productos'. Lista nunca
vacía
test_metrics.py metrics.py Estado CRÍTICO, BAJO, NORMAL.
Lista vacía devuelve zeros
test_valuation.py valuation.py Valor correcto (precio × stock), producto
sin BD devuelve 0, lista vacía = 0.0
test_recommender.py recommender.py
Lista crítica genera recomendación
urgente, lista normal genera OK
test_demand_analyzer.py demand_analyzer.py
Media correcta, historial vacío lanza
ValueError, historial de un elemento
test_stock_predictor.py stock_predictor.py
Mock de historial, días correctos, estado
correcto por rango
test_full_pipeline.py Integración completa
detect → predict → recommend no
lanza excepciones, resultado tiene
claves esperadas
5.2 — Formato obligatorio de docstring en tests
def test_calculate_daily_demand_con_historial_normal():
"""Verifica que la demanda diaria se calcula correctamente.
Args: Ninguno.
Fundación Dicampus · Inclusión Socio-Laboral | Página 9
InventarioMarketTalento
Returns: None.
Example:

> > > result = calculate_daily_demand([3, 4, 5])
> > > result == 4.0
> > > True
> > > """

# Arrange

historial = [3, 4, 5, 4, 3, 5, 4, 3, 4, 5]

# Act

resultado = calculate_daily_demand(historial)

# Assert

assert resultado == 4.0
Regla de oro: Si no tienes docstring en el test, el commit no es válido. Usa la IA para generar
el esqueleto y completa los ejemplos tú mismo/a.
