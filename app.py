import streamlit as st
import os

st.set_page_config(
    page_title="Sentinela Oculto v3.2",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def carregar_css():
    caminho_css = os.path.join("assets", "style.css")
    if os.path.exists(caminho_css):
        with open(caminho_css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css()

st.title("🛡️ Projeto Sentinela Oculto v3.2")
st.subheader("Painel Interativo de Intuição Computacional e Defesa Preditiva")

# O 'r' antes das aspas resolve o problema das letras gregas (\alpha, \beta)
st.markdown(r"""
---
Bem-vindo ao ambiente de simulação técnica do **Projeto Sentinela Oculto**.

Este dashboard foi desenvolvido para tangibilizar a arquitetura cognitiva estocástica do projeto, traduzindo as equações e modelos matemáticos propostos no documento acadêmico em uma prova de conceito interativa. 

Utilize o **menu de navegação lateral** para explorar as funcionalidades modulares:

* **1. Simulador do Motor TIS:** Calibre os pesos estatísticos ($\alpha, \beta, \gamma, \delta$) e simule o cálculo do *Threat Intuition Score* diante de anomalias ($A(x)$) e probabilidades Bayesianas ($B(e)$).
* **2. Timeline de Ameaças Furtivas:** Acompanhe a dissecação temporal do "Cenário 2: Insider Threat" usando o Módulo UEBA e o Hidden Markov Model (HMM).
* **3. Calibração vs Fadiga Analítica:** Veja como o algoritmo ADWIN mitiga o excesso de falsos positivos gerados por regras estáticas tradicionais.

---
**Pesquisa e Arquitetura:** Anderson Capelini Andrade  
**Instituição:** FATEC Cotia (Ciência de Dados - 4º Semestre)
""")