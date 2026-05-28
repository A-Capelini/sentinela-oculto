import plotly.graph_objects as go

def plotar_velocimetro_tis(valor):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=valor,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Threat Intuition Score (TIS)", 'font': {'size': 18, 'color': '#333333'}},
        gauge={
            'axis': {'range': [0, 1.0], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#333333"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 0.5], 'color': "#d9f2d9"},
                {'range': [0.5, 0.8], 'color': "#fff2cc"},
                {'range': [0.8, 1.0], 'color': "#f2d9d9"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 0.8 
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor="#FAF9F6", font={'color': "#333333"})
    return fig

def plotar_velocimetro_cs(valor):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=valor,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Confidence Score (CS)", 'font': {'size': 18, 'color': '#333333'}},
        gauge={
            'axis': {'range': [0, 1.0]},
            'bar': {'color': "#4E0707"}, 
            'bgcolor': "white",
            'steps': [
                {'range': [0, 0.4], 'color': "#e6e6e6"}, 
                {'range': [0.4, 0.7], 'color': "#cccccc"}, 
                {'range': [0.7, 1.0], 'color': "#999999"} 
            ]
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor="#FAF9F6", font={'color': "#333333"})
    return fig

def plotar_comparativo_fadiga(adwin_ativado):
    """
    Gera um gráfico de barras comparando o volume de alertas de um SIEM tradicional
    contra a inteligência do Sentinela Oculto com o ADWIN ativado.
    """
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    
    # Simulação de um pico de tráfego legítimo (ex: fechamento de folha de pagamento na Quarta)
    alertas_siem = [120, 140, 890, 750, 135]
    
    if adwin_ativado:
        # Com ADWIN, o sistema reconhece o novo padrão normal (Concept Drift) e não gera falsos alertas
        alertas_sentinela = [15, 18, 25, 20, 12]
        cor_sentinela = "#4E0707" # Borgonha Forte
    else:
        # Sem ADWIN, o Sentinela se comporta como um SIEM cego, gerando fadiga analítica
        alertas_sentinela = [115, 135, 870, 720, 125]
        cor_sentinela = "#e6b3b3" # Borgonha Desbotado (Alerta de Falha)

    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=dias, y=alertas_siem,
        name='SIEM Tradicional (Regras Estáticas)',
        marker_color='#cccccc'
    ))
    
    fig.add_trace(go.Bar(
        x=dias, y=alertas_sentinela,
        name='Sentinela Oculto',
        marker_color=cor_sentinela
    ))

    fig.update_layout(
        title='Volume de Alertas no SOC (Falsos Positivos vs Ameaças Reais)',
        barmode='group',
        paper_bgcolor="#FAF9F6",
        plot_bgcolor="#FAF9F6",
        font={'color': "#333333"},
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)')
    )
    
    return fig