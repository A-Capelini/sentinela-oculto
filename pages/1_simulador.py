import streamlit as st
import os
import sys

# Garante que a subpágina consiga enxergar as pastas 'core' e 'components'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.motor_tis import calcular_tis, calcular_confidence_score
from components.graficos import plotar_velocimetro_tis, plotar_velocimetro_cs

st.set_page_config(page_title="Simulador TIS", page_icon="⚙️", layout="wide")

st.title("⚙️ Simulador do Threat Intuition Score (TIS)")
st.markdown("Ajuste os pesos arquitetônicos e os sinais de telemetria para observar a inferência matemática em tempo real.")
st.markdown("---")

col_pesos, col_sinais = st.columns(2)

with col_pesos:
    st.subheader("1. Pesos da Arquitetura")
    st.info("A soma deve ser 1.0. O motor recalibrará automaticamente se for diferente.")
    alpha = st.slider("Alpha (α) - Isolation Forest", 0.0, 1.0, 0.25, 0.05)
    beta = st.slider("Beta (β) - Rede Bayesiana", 0.0, 1.0, 0.25, 0.05)
    gamma = st.slider("Gamma (γ) - HMM Sequencial", 0.0, 1.0, 0.25, 0.05)
    delta = st.slider("Delta (δ) - Perfil UEBA", 0.0, 1.0, 0.25, 0.05)

with col_sinais:
    st.subheader("2. Entradas dos Sensores (Ameaça)")
    st.warning("Simule o nível de anomalia captado por cada nível cognitivo (0 = Normal, 1 = Ataque Crítico).")
    a_x = st.slider("A(x) - Anomalia Instantânea", 0.0, 1.0, 0.10, 0.01)
    b_e = st.slider("B(e) - Suspeita Bayesiana", 0.0, 1.0, 0.10, 0.01)
    t_s = st.slider("T(s) - Transição Oculta (HMM)", 0.0, 1.0, 0.10, 0.01)
    u_r = st.slider("U(r) - Desvio de Perfil (UEBA)", 0.0, 1.0, 0.10, 0.01)

st.markdown("---")

# Cálculo executado pelo Motor
resultado_tis = calcular_tis(alpha, beta, gamma, delta, a_x, b_e, t_s, u_r)
resultado_cs = calcular_confidence_score(a_x, b_e, t_s, u_r)

st.subheader("Painel de Decisão Automatizada")

# Substituímos as métricas simples pelos gráficos do Plotly
col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    fig_tis = plotar_velocimetro_tis(resultado_tis)
    st.plotly_chart(fig_tis, use_container_width=True)
    
    # Lógica de Alertas abaixo do gráfico
    if resultado_tis > 0.8:
        st.error("🚨 **AÇÃO:** Bloqueio Lógico Preventivo Acionado (Isolamento de Host)")
    elif resultado_tis > 0.5:
        st.warning("⚠️ **AÇÃO:** Alerta Prioritário gerado para o SOC")
    else:
        st.success("✅ **AÇÃO:** Tráfego Legítimo. Nenhuma ação necessária.")

with col_grafico2:
    fig_cs = plotar_velocimetro_cs(resultado_cs)
    st.plotly_chart(fig_cs, use_container_width=True)
    
    if resultado_cs < 0.5:
        st.info("ℹ️ **Contexto:** Sensores divergentes. Aumentando o peso da calibração manual.")
    else:
        st.info("ℹ️ **Contexto:** Alta sinergia entre os sensores.")