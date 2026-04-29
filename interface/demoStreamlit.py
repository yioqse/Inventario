import streamlit as st
import pandas as pd
import sys
import os

# Fix for ModuleNotFoundError when running from different directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.database.db_reader import get_product_info
from services.vision.detector import detect_products
from services.inventory.metrics import count_by_status
from services.inventory.valuation import calculate_inventory_value
from services.database.db_filter import get_sales_history
from services.prediction.stock_predictor import predict_stock_outage
from services.inventory.recommender import generate_recommendations

st.set_page_config(page_title='Markettalento Inventario', page_icon='📦', layout='wide')
st.title('📦 Sistema de Inventario — Markettalento')

if st.button('🔍 Analizar Inventario'):
    with st.spinner("Escaneando bodega..."):
        deteccion = detect_products()
        productos = deteccion.get('productos', [])
        st.success(f"✅ {deteccion.get('descripcion', 'Detección completada')}")
        
        # --- Sección A — Resultados del Análisis ---
        st.header("Sección A — Resultados del Análisis")
        metricas = count_by_status(productos)
        resumen = metricas["resumen"]
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric('Productos Detectados', resumen['total_productos'])
        col2.metric('Unidades Totales', resumen['total_unidades'])
        col3.metric('Productos Críticos', resumen['productos_criticos'])
        col4.metric('Stock Bajo', resumen['productos_bajos'])
        
        # --- Sección B — Detalle del Análisis ---
        st.header('Sección B — Detalle del Análisis')
        filas = []
        productos_para_recomendar = []
        
        for p in productos:
            nombre = p["nombre"]
            stock = p["cantidad"]
            info = get_product_info(nombre)
            
            if info:
                historial = get_sales_history(nombre, days=30)
                try:
                    pred = predict_stock_outage(historial, stock, info)
                    estado = pred["estado"]
                    dias = pred["dias_hasta_agotarse"]
                except ValueError:
                    estado = "SIN HISTORIAL"
                    dias = "N/A"
                
                stock_min = info.get("stock_minimo", 5)
                item_rec = {"producto": nombre, "stock_actual": stock, "stock_minimo": stock_min}
                
                # Recomendación individual para la tabla
                if stock <= stock_min:
                    productos_para_recomendar.append(item_rec)
                    rec_result = generate_recommendations([item_rec])
                    recomendacion = rec_result[0]["recomendacion"] if rec_result else "Reponer"
                else:
                    recomendacion = "OK"
                
                filas.append({
                    "Producto": nombre,
                    "Stock Actual": stock,
                    "Estado": estado,
                    "Días hasta Agotarse": dias,
                    "Recomendación": recomendacion
                })
            else:
                # Si el producto no está en DB, lo mostramos con error para depuración
                filas.append({
                    "Producto": f"{nombre} (No en DB)",
                    "Stock Actual": stock,
                    "Estado": "ERROR",
                    "Días hasta Agotarse": "N/A",
                    "Recomendación": "Verificar DB"
                })
        
        if filas:
            st.dataframe(pd.DataFrame(filas), width='stretch')

        
        # --- Sección C — Recomendaciones de Reposición y Valor del Inventario ---
        st.header('Sección C — Recomendaciones de Reposición y Valor del Inventario')
        
        st.subheader('🚨 Recomendaciones de Reposición')
        recs_globales = generate_recommendations(productos_para_recomendar)
        if recs_globales:
            for r in recs_globales:
                st.error(f"**{r['producto']}**: {r['recomendacion']}")
        else:
            st.success("✅ Todo en orden. No hay recomendaciones críticas.")
            
        st.subheader('💰 Valor del Inventario')
        valor = calculate_inventory_value(productos)
        st.metric('Valor Total', f'{valor:.2f} €')
