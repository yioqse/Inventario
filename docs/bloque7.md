### BLOQUE 7 — Interfaz Streamlit:

El archivo interface/demoStreamlit.py es la única interfaz de usuario del proyecto. Reemplaza
completamente el HTML embebido de Flask. Importa exclusivamente de services/ y no contiene lógica de negocio.

# 7.1 — Secciones obligatorias del dashboard

# Sección A — Resultados del Análisis (métricas con st.metric)

Productos
Detectados
Unidades Totales
Productos Críticos
Stock Bajo
5 34 0 2

# Sección B — Detalle del Análisis (tabla con st.dataframe)

Producto
Stock
Actual
Estado
Días hasta Agotarse
Recomendación
Leche Entera 8 Normal 2 Monitorear
Huevos M 2 Bajo 0.7 Reponer urgente
Pan de Molde 3 Crítico 0.3 Reponer YA
Agua Mineral 12 Normal 1.1 OK
Café Molido 6 Normal 4.0 Monitorear

# Sección C — Recomendaciones de Reposición y Valor del Inventario

• 🚨 Recomendaciones de Reposición: lista de productos con estado Crítico o Bajo, con mensaje
de acción claro
• 💰 Valor del Inventario: suma de (stock × precio) para todos los productos detectados,
formateado con 2 decimales y símbolo €

# 7.2 — Fragmento de referencia Streamlit

import streamlit as st
import pandas as pd
from services.database.product_db import product_database
from services.database.db_reader import get_all_products
from services.vision.detector import detect_products
from services.inventory.metrics import count_by_status
from services.inventory.valuation import calculate_inventory_value
from services.inventory.recommender import generate_recommendations
from services.prediction.stock_predictor import predict_stock_outage
st.set_page_config(page_title='Markettalento Inventario', page_icon='📦',
layout='wide')
st.title('📦 Sistema de Inventario — Markettalento')

if st.button('🔍 Analizar Inventario'):
deteccion = detect_products()
productos = deteccion['productos']

# Sección A — Métricas

metricas = count_by_status(productos, product_database)
col1, col2, col3, col4 = st.columns(4)
col1.metric('Productos Detectados', metricas['total'])
col2.metric('Unidades Totales', metricas['total_unidades'])
col3.metric('Productos Críticos', metricas['criticos'])
col4.metric('Stock Bajo', metricas['bajos'])

# Sección B — Tabla de detalle

st.subheader('📊 Detalle del Análisis')
filas = []
for p in productos:
pred = predict_stock_outage(p, product_database)
rec = generate_recommendations([pred]) if pred['estado'] != 'Normal' else
'OK'
filas.append({...})
st.dataframe(pd.DataFrame(filas), use_container_width=True)

# Sección C — Recomendaciones y valor

st.subheader('🚨 Recomendaciones de Reposición')

# ... mostrar productos que necesitan reposición

st.subheader('💰 Valor del Inventario')
valor = calculate_inventory_value(productos, product_database)
st.metric('Valor Total', f'{valor:.2f} €')

RP en la interfaz: demoStreamlit.py no debe contener ninguna lógica de negocio. Si copias una
fórmula de cálculo dentro de demoStreamlit.py, estás violando el SRP. Toda la lógica vive en
services/. La interfaz solo llama funciones y muestra resultados
