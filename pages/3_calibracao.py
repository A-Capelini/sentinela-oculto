import streamlit as st
import os
import sys

# Garante a importação dos componentes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.graficos import plotar_comparativo_fadiga

st.set_page_config(page_title="Mitigação de Fadiga", page_icon="⚖️", layout="wide")

def carregar_css():
    caminho_css = os.path.join("assets", "style.css")
    if os.path.exists(caminho_css):
        with open(caminho_css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css()

st.title("⚖️ Calibração de Pesos vs Fadiga Analítica")
st.markdown("Demonstração prática de como a imunização contra a Deriva Conceitual (*Concept Drift*) protege o Centro de Operações de Segurança (SOC) contra o excesso de falsos positivos.")
st.markdown("---")

col_texto, col_grafico = st.columns([1, 1.8])

with col_texto:
    st.subheader("O Paradoxo das Regras Estáticas")
    st.markdown("""
    Sistemas SIEM tradicionais entram em colapso quando o comportamento da rede muda legitimamente (Ex: pico de acessos sistêmicos em dia de fechamento de folha de pagamento).
    
    No **Projeto Sentinela Oculto**, essa fadiga é mitigada ativando o mecanismo de **Calibração Dinâmica** (Algoritmo ADWIN), que percebe a mudança de tendência e recalibra a verossimilhança Bayesiana automaticamente.
    """)
    
    st.markdown("### Controle do Motor")
    
    # Toggle interativo para simular a inteligência do sistema
    adwin_ativado = st.toggle("🧠 Ativar Algoritmo ADWIN (Calibração Dinâmica)", value=False)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if adwin_ativado:
        st.success("✅ **STATUS:** ADWIN Ativado.\n\nO sistema compreendeu que o pico de tráfego na Quarta e Quinta-feira é um fluxo corporativo legítimo. A *baseline* foi recalibrada e centenas de falsos positivos foram suprimidos.")
    else:
        st.warning("⚠️ **STATUS:** ADWIN Desativado (Modo Estático).\n\nO motor está operando de forma engessada. A alteração legítima de tráfego está gerando uma avalanche de alertas inúteis, causando fadiga no analista.")

with col_grafico:
    # Renderiza o gráfico baseado na escolha do Toggle
    fig = plotar_comparativo_fadiga(adwin_ativado)
    st.plotly_chart(fig, use_container_width=True)