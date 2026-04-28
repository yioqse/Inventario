import streamlit as st
import pandas as pd
from services.database.db_reader import get_all_products
from services.vision.detector import detect_products
from services.inventory.metrics import count_by_status
from services.inventory.valuation import calculate_inventory_value

st.set_page_config(page_title="Sistema de Inventario Inteligente", page_icon="📦", layout="wide")

st.title("📦 Sistema de Inventario Inteligente")
st.markdown("Análisis con Visión Artificial y Predicción de Demanda")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("🔌 Acciones")
    
    if st.button("🔍 Analizar Inventario (Simulado)"):
        with st.spinner("Analizando imagen..."):
            deteccion = detect_products()
            productos_detectados = deteccion.get("productos", [])
            
            st.success(f"✅ Detección completada: {deteccion['descripcion']}")
            
            # Métricas
            analisis = count_by_status(productos_detectados)
            valor_inventario = calculate_inventory_value(productos_detectados)
            
            st.metric("Total Productos", analisis["resumen"]["total_productos"])
            st.metric("Valor del Inventario", f"${valor_inventario}")
            st.metric("Productos Críticos", analisis["resumen"]["productos_criticos"])

with col2:
    st.header("📋 Catálogo de Productos (Base de Datos)")
    productos = get_all_products()
    if productos:
        df = pd.DataFrame(productos)
        # Seleccionar columnas relevantes
        df = df[['id', 'nombre', 'categoria', 'precio', 'stock_minimo']]
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay productos en la base de datos.")
