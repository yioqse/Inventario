# Primeros Pasos:

analizados los ficheros y creado el main.py para posterior refactorizacion
instaladas librerias necesarias
crear requirements.txt -> lo tengo en el repositorio

ejecutarlo
todo correcto -> funciona main.py
1er commit

# Union de paneles y refactorización

analiza los ficheros heredados InventarioAlfa.py y EndPoin_Api.py, dime que errores tiene y como arreglarlos. de momento he visto estos: Problemas conocidos: (1) Monolito sin separación de capas. (2) HTML embebido. (3) Violación
del SRP en todas las funciones. (4) Sin type hints. (5) Sin docstrings. (6) Sin tests. (7) Base de datos
con solo 11 productos en 5 categorías mezcladas. Tu misión es refactorizar respetando el SRP
aunque eso genere más archivos y carpetas. para la refactorizacion he creado el main.py el cual debe ser el principal

He intentado añadir los Endpoints del fichero EndPoin_Api.py al main.py pero da muchos errores.

planifica la refactorizacion y dime como proceder
creacion de .gitignore y estructura de carpetas

# estructura de proyecto

+-- services/ # Toda la lógica de negocio
| +-- **init**.py
| +-- database/ # Responsabilidad: datos
| +-- **init**.py
| +-- product_db.py # Solo los datos: los 25 productos
| +-- db_reader.py # Solo lectura: get_product_info(), get_all_products()
| +-- db_filter.py # Solo filtrado: get_by_category(), get_sales_history()
| +-- vision/ # Responsabilidad: detección de imagen
| +-- **init**.py
| +-- detector.py # Solo orquestación: detect_products()
| +-- scenario_loader.py # Solo escenarios: \_load_scenarios()
| +-- inventory/ # Responsabilidad: análisis de inventario
| +-- **init**.py
| +-- metrics.py # Solo métricas: count_by_status()
| +-- valuation.py # Solo valoración: calculate_inventory_value()
| +-- recommender.py # Solo recomendaciones:
generate_recommendations()
| +-- prediction/ # Responsabilidad: predicción de demanda
| +-- **init**.py
| +-- stock_predictor.py # Solo predicción: predict_stock_outage()
| +-- demand_analyzer.py # Solo análisis: calculate_daily_demand()
+-- interface/ # Responsabilidad: presentación
| +-- demoStreamlit.py # Solo la UI Streamlit
+-- tests/ # Responsabilidad: verificación
| +-- **init**.py
| +-- services/
| +-- database/
| +-- test_product_db.py
| +-- test_db_reader.py
| +-- test_db_filter.py
| +-- vision/
| +-- test_detector.py
| +-- test_scenario_loader.py
| +-- inventory/
| +-- test_metrics.py
| +-- test_valuation.py
| +-- test_recommender.py
| +-- prediction/
| +-- test_stock_predictor.pyactualmente tengo esta estructura
+-- test_demand_analyzer.py
| +-- integration/
| +-- test_full_pipeline.py
+-- docs/
| +-- arquitectura.md # Diagrama y descripción de módulos
| +-- Final.md # Memoria de cambios realizados
+-- .github/
| +-- workflows/
| +-- ci.yml # Matriz: Python 3.9 / 3.10 / 3.11 / 3.12
+-- requirements.txt
+-- .gitignore # **pycache**, .venv, \*.pyc
+-- README.md # Instalación, uso, sección IA, badge CI

commit2: .gitignore, estructura y refactorizacion
pero no funciona main
modifico el main y el html
