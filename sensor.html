# app.py
import streamlit as st
import random
import datetime
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Sistema Eco ESP32", layout="wide")

# === HEADER ===
st.markdown("""
    <h1 style='text-align: center; color: #2e7d32;'>🌱 Sistema de Monitoreo Eco ESP32</h1>
    <p style='text-align: center; color: #388e3c;'>Monitoreo inteligente de ambiente y suelo en tiempo real</p>
    """, unsafe_allow_html=True)

# Estado de conexión simulado
estado = random.choice(["En línea", "Desconectado"])
color = "#4caf50" if estado == "En línea" else "#f44336"
st.markdown(f"<div style='text-align:center; color:{color}; font-weight:600;'>🔌 Estado del sistema: {estado}</div>", unsafe_allow_html=True)

st.markdown("---")

# === SENSOR DATA ===
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
    badge_color = "green" if on else "gray"
    st.markdown(f"""
        <div style='text-align:center;'>
            <div style='font-size:2rem'>{emoji}</div>
            <strong style='color:#2e7d32;'>{nombre}</strong><br>
            <span style='background:{badge_color}; color:white; padding:8px 20px; border-radius:25px;'>{status}</span>
        </div>
    """, unsafe_allow_html=True)

with col3:
    estado_dispositivo("Bomba de Agua", "💧")

with col4:
    estado_dispositivo("Ventilador", "🌀")

with col5:
    estado_dispositivo("LED Temperatura", "💡")

st.markdown("---")

# === GRÁFICO DE LECTURAS ===
st.subheader("📊 Histórico de Sensores")
fechas = [datetime.datetime.now() - datetime.timedelta(minutes=5*i) for i in range(20)][::-1]
df = pd.DataFrame({
    "Hora": [f.strftime("%H:%M") for f in fechas],
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

# === TABLA DE DATOS HISTÓRICOS ===
st.subheader("📋 Datos Históricos Recientes")
df_tabla = df.copy()
df_tabla["Bomba"] = [random.choice(["Encendida", "Apagada"]) for _ in range(len(df))]
df_tabla["Ventilador"] = [random.choice(["Encendido", "Apagado"]) for _ in range(len(df))]
df_tabla["LED"] = [random.choice(["Encendido", "Apagado"]) for _ in range(len(df))]
st.dataframe(df_tabla.tail(10), use_container_width=True)

# === Última actualización ===
st.markdown(f"<div style='text-align:center; color:#388e3c;'>🕐 Última actualización: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)

