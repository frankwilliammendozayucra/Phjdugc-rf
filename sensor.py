import streamlit as st
import random
import datetime
import pandas as pd
import plotly.graph_objects as go
import time

# Configuración de la página
st.set_page_config(page_title="Sistema Eco ESP32", layout="wide")

# Contenedor de actualización
placeholder = st.empty()

# Bucle principal de visualización (se recarga con experimental_rerun)
for _ in range(1):
    with placeholder.container():
        # === TÍTULO ===
        st.markdown("""
            <h1 style='text-align: center; color: #2e7d32;'>🌱 Sistema de Monitoreo Eco ESP32</h1>
            <p style='text-align: center; color: #388e3c;'>Monitoreo inteligente de ambiente y suelo en tiempo real</p>
        """, unsafe_allow_html=True)

        estado = random.choice(["En línea", "Desconectado"])
        color = "#4caf50" if estado == "En línea" else "#f44336"
        st.markdown(f"<div style='text-align:center; color:{color}; font-weight:600;'>🔌 Estado del sistema: {estado}</div>", unsafe_allow_html=True)

        st.markdown("---")

        # === SENSORES ===
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🌤️ Sensores Ambientales")
            temp_amb = round(random.uniform(20, 30), 1)
            hum_amb = round(random.uniform(40, 70), 1)
            st.metric("🌡️ Temperatura Ambiental", f"{temp_amb} °C")
            st.metric("💨 Humedad Ambiental", f"{hum_amb} %")

        with col2:
            st.subheader("🌱 Sensores del Suelo")
            hum_suelo = round(random.uniform(30, 80), 1)
            raw = random.randint(300, 900)
            st.metric("🏔️ Humedad del Suelo", f"{hum_suelo} %")
            st.metric("📊 Valor RAW", f"{raw} ADC")

        st.markdown("---")

        # === ESTADO DE DISPOSITIVOS ===
        st.subheader("⚡ Estado de Dispositivos")
        col3, col4, col5 = st.columns(3)

        def estado_dispositivo(nombre, emoji):
            on = random.choice([True, False])
            status = "Encendido" if on else "Apagado"
            bgcolor = "#2E7D32" if on else "#616161"
            st.markdown(f"""
                <div style='text-align:center; margin-bottom:20px;'>
                    <div style='font-size:2.5rem;'>{emoji}</div>
                    <div style='font-weight:600; color:#2e7d32; margin-top:5px;'>{nombre}</div>
                    <div style='display:inline-block; background:{bgcolor}; color:white;
                                padding:6px 22px; border-radius:20px; font-size:0.9rem;
                                margin-top:8px;'>
                        {status}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            estado_dispositivo("Bomba de Agua", "💧")
        with col4:
            estado_dispositivo("Ventilador", "🌀")
        with col5:
            estado_dispositivo("LED Temperatura", "💡")

        st.markdown("---")

        # === GRÁFICO ===
        st.subheader("📊 Histórico de Sensores")
        fechas = [datetime.datetime.now() - datetime.timedelta(seconds=5*i) for i in range(20)][::-1]
        df = pd.DataFrame({
            "Hora": [f.strftime("%H:%M:%S") for f in fechas],
            "Temperatura": [random.uniform(20, 30) for _ in fechas],
            "Humedad Ambiental": [random.uniform(40, 70) for _ in fechas],
            "Humedad Suelo": [random.uniform(30, 80) for _ in fechas]
        })

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Hora"], y=df["Temperatura"], mode='lines+markers', name='🌡️ Temp. Ambiental'))
        fig.add_trace(go.Scatter(x=df["Hora"], y=df["Humedad Ambiental"], mode='lines+markers', name='💨 Humedad Amb.'))
        fig.add_trace(go.Scatter(x=df["Hora"], y=df["Humedad Suelo"], mode='lines+markers', name='🏔️ Humedad Suelo'))

        fig.update_layout(xaxis_title="Hora", yaxis_title="Valor", legend_title="Sensor", height=400)
        st.plotly_chart(fig, use_container_width=True)

        # === TABLA ===
        st.subheader("📋 Datos Históricos Recientes")
        df_tabla = df.copy()
        df_tabla["Bomba"] = [random.choice(["Encendida", "Apagada"]) for _ in range(len(df))]
        df_tabla["Ventilador"] = [random.choice(["Encendido", "Apagado"]) for _ in range(len(df))]
        df_tabla["LED"] = [random.choice(["Encendido", "Apagado"]) for _ in range(len(df))]
        st.dataframe(df_tabla.tail(10), use_container_width=True)

        # === FOOTER ===
        st.markdown(f"<div style='text-align:center; color:#388e3c;'>🕐 Última actualización: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)

    # Pausa de 5 segundos y recarga
    time.sleep(5)
    st.experimental_rerun()

