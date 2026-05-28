import numpy as np

def calcular_tis(alpha, beta, gamma, delta, a_x, b_e, t_s, u_r):
    soma_pesos = alpha + beta + gamma + delta
    if soma_pesos == 0:
        return 0.0
        
    a = alpha / soma_pesos
    b = beta / soma_pesos
    g = gamma / soma_pesos
    d = delta / soma_pesos
    
    tis = (a * a_x) + (b * b_e) + (g * t_s) + (d * u_r)
    return round(tis, 3)

def calcular_confidence_score(a_x, b_e, t_s, u_r):
    sinais = [a_x, b_e, t_s, u_r]
    desvio_padrao = np.std(sinais)
    cs = max(0.0, 1.0 - (desvio_padrao * 2))
    return round(cs, 3)