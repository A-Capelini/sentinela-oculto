import streamlit as st
import os
import sys
import json

# Garante a importação do core e components
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.motor_tis import calcular_tis
from components.graficos import plotar_velocimetro_tis

st.set_page_config(page_title="Timeline Narrativa", page_icon="⏱️", layout="wide")

def carregar_css():
    caminho_css = os.path.join("assets", "style.css")
    if os.path.exists(caminho_css):
        with open(caminho_css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css()

# Função para carregar os dados JSON
def carregar_dados():
    caminho_json = os.path.join("data", "telemetria_mock.json")
    with open(caminho_json, 'r', encoding='utf-8') as f:
        return json.load(f)["insider_threat"]

dados_timeline = carregar_dados()

# Inicialização do estado de tempo (Session State)
if 'passo_tempo' not in st.session_state:
    st.session_state.passo_tempo = 0

# Lógica dos Botões de Navegação no Tempo
def avancar_tempo():
    if st.session_state.passo_tempo < len(dados_timeline) - 1:
        st.session_state.passo_tempo += 1

def resetar_tempo():
    st.session_state.passo_tempo = 0

# Cabeçalho
st.title("⏱️ Dissecação Temporal: Insider Threat")
st.markdown("Acompanhe como a **Memória Episódica (UEBA)** e o **HMM** correlacionam sinais fracos ao longo de 5 dias (Cenário 2 do Documento Oficial).")
st.markdown("---")

col_narrativa, col_painel = st.columns([1.2, 1])

# Obtém o momento atual baseado no clique do usuário
momento_atual = dados_timeline[st.session_state.passo_tempo]

with col_narrativa:
    st.subheader(f"📅 {momento_atual['dia']}")
    
    st.markdown(f"**Ação Operacional:** {momento_atual['evento']}")
    st.markdown(f"**Sinal Técnico:** {momento_atual['sinal']}")
    
    st.info(f"🧠 **Contexto Cognitivo:** {momento_atual['desc_tecnica']}")
    
    st.markdown("---")
    
    # Controles de Tempo
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.button("⏳ Avançar no Tempo", on_click=avancar_tempo, use_container_width=True, disabled=(st.session_state.passo_tempo == len(dados_timeline) - 1))
    with col_btn2:
        st.button("🔄 Reiniciar Simulação", on_click=resetar_tempo, use_container_width=True)

with col_painel:
    # Coleta os pesos e sensores do JSON para calcular o TIS real no Motor
    p = momento_atual['pesos_sugeridos']
    s = momento_atual['sensores']
    
    tis_calculado = calcular_tis(p['alpha'], p['beta'], p['gamma'], p['delta'], s['ax'], s['be'], s['ts'], s['ur'])
    
    # Renderiza o velocímetro passando o valor calculado
    fig_tis = plotar_velocimetro_tis(tis_calculado)
    st.plotly_chart(fig_tis, use_container_width=True)
    
    # Caixa de Ação baseada no limite paramétrico (0.80)
    if tis_calculado >= 0.8:
        st.error("🚨 **AÇÃO:** TIS Crítico. Congelamento de Credenciais Executado!")
    elif tis_calculado >= 0.5:
        st.warning("⚠️ **AÇÃO:** Nível de Suspeita Elevado. Ajuste de Prior no Motor Bayesiano.")
    else:
        st.success("✅ **AÇÃO:** Sinais fracos armazenados na memória. Nenhuma intervenção de bloqueio.")