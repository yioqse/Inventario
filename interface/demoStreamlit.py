import streamlit as st
import pandas as pd
from services.database.db_reader import get_all_products, get_product_info
from services.vision.detector import detect_products
from services.inventory.metrics import count_by_status
from services.inventory.valuation import calculate_inventory_value
from services.database.db_filter import get_sales_history
from services.prediction.stock_predictor import predict_stock_outage
from services.inventory.recommender import generate_recommendations

st.set_page_config(page_title="Smart Inventory", page_icon="📦", layout="wide")

st.title("📦 Sistema de Inventario Inteligente (Demo)")
st.markdown("Plataforma interactiva que orquesta los microservicios del backend.")

# --- SECCIÓN 1: CATÁLOGO ---
st.header("1️⃣ Catálogo de Productos (Database)")
productos = get_all_products()
if productos:
    df = pd.DataFrame(productos)[['id', 'nombre', 'categoria', 'precio', 'stock_minimo']]
    st.dataframe(df, use_container_width=True)

# --- SECCIÓN 2: VISIÓN ARTIFICIAL ---
st.header("2️⃣ Detección por Visión Artificial (Vision & Metrics)")
if st.button("🔍 Escanear Bodega (Simulación)", type="primary"):
    with st.spinner("Procesando imágenes de las cámaras..."):
        deteccion = detect_products()
        productos_detectados = deteccion.get("productos", [])
        
        st.success(f"Detección completada: {deteccion['descripcion']}")
        
        # Cálculos de inventario
        analisis = count_by_status(productos_detectados)
        valor_inventario = calculate_inventory_value(productos_detectados)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Artículos", analisis["resumen"]["total_productos"])
        c2.metric("Valor del Inventario", f"${valor_inventario}")
        c3.metric("Bajos en Stock", analisis["resumen"]["productos_criticos"])

        st.dataframe(pd.DataFrame(productos_detectados), use_container_width=True)
        
        # Guardar estado para el paso 3
        st.session_state['detectados'] = productos_detectados

# --- SECCIÓN 3: PREDICCIÓN Y RECOMENDACIÓN ---
st.header("3️⃣ Prevención y Decisiones (Prediction & Recommender)")
if st.button("🔮 Analizar Tendencias y Generar Recomendaciones"):
    if 'detectados' not in st.session_state:
        st.warning("⚠️ Primero debes realizar el escaneo en el Paso 2.")
    else:
        with st.spinner("Analizando histórico y calculando previsiones..."):
            predicciones = []
            para_recomendar = []
            
            for p in st.session_state['detectados']:
                nombre = p["nombre"]
                stock = p["cantidad"]
                info = get_product_info(nombre)
                
                if info:
                    # Inyectar historial y predecir
                    historial = get_sales_history(nombre, days=30)
                    try:
                        pred = predict_stock_outage(historial, stock, info)
                        estado = pred["estado"]
                        dias = pred.get("dias_para_agotarse", "N/A")
                    except ValueError:
                        estado = "SIN HISTORIAL ⚠️"
                        dias = "N/A"
                    
                    predicciones.append({
                        "Producto": nombre,
                        "Stock Actual": stock,
                        "Días p/ Agotar": dias,
                        "Estado Predictivo": estado
                    })
                    
                    # Preparar lista para el recomendador si es necesario
                    stock_min = info.get("stock_minimo", 5)
                    if stock <= stock_min:
                        para_recomendar.append({
                            "producto": nombre,
                            "stock_actual": stock,
                            "stock_minimo": stock_min
                        })
            
            # Mostrar tabla predictiva
            st.subheader("Análisis Predictivo de Demanda")
            st.table(pd.DataFrame(predicciones))
            
            # Acción del recomendador
            st.subheader("Acciones Recomendadas Automáticas")
            recomendaciones = generate_recommendations(para_recomendar)
            if recomendaciones:
                for r in recomendaciones:
                    st.error(f"🚨 **{r['producto']}**: {r['accion']}")
            else:
                st.success("✅ ¡El inventario está en niveles óptimos de proyección! No se requieren compras de urgencia.")
