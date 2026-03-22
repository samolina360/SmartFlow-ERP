import streamlit as st
from app.models.product import Producto

# 1. Configuración de la página (Lo que se ve en la pestaña del navegador)
st.set_page_config(page_title="SmartFlow ERP - Demo", page_icon="📦")

st.title("🚀 SmartFlow ERP")
st.subheader("Sistema de Gestión de Inventario (Demo)")

# 2. Inicializar un producto en la "memoria" de la web
# Usamos session_state para que el stock no se reinicie cada vez que pulsas un botón
if 'mi_producto' not in st.session_state:
    p = Producto(1, "Laptop Pro", 800.0, 1200.0)
    p.registrar_movimiento('entrada', 50) # Stock inicial de 50
    st.session_state.mi_producto = p

prod = st.session_state.mi_producto

# 3. Diseño de la Interfaz (Métricas)
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Producto", value=prod.nombre)
    st.metric(label="Stock Actual", value=f"{prod.stock} unidades")
with col2:
    st.metric(label="Precio Venta", value=f"${prod.precio}")
    st.metric(label="Margen de Ganancia", value=f"${prod.obtener_margen()}")

st.divider()

# 4. Sección de Acciones (Ventas)
st.write("### 🛒 Registrar Operación")
cantidad = st.number_input("Cantidad a vender", min_value=1, max_value=int(prod.stock), step=1)

if st.button("Realizar Venta"):
    if prod.stock >= cantidad:
        prod.registrar_movimiento('salida', cantidad)
        st.success(f"✅ Venta exitosa: Se vendieron {cantidad} unidades.")
        st.balloons() # ¡Efecto visual para impresionar!
        st.rerun()    # Recarga para actualizar las métricas arriba
    else:
        st.error("❌ Error: Stock insuficiente para realizar la venta.")

# 5. Pie de página profesional
st.sidebar.info("Desarrollado por Sebastian Molina - Arquitectura MVC")