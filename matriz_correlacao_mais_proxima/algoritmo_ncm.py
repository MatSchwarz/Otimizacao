import numpy as np
from func_auxiliares_ncm import *


def atualiza_diag_x(x, g):
    """Função responsável por fazer uma iteração do algoritmo"""
    df = np.linalg.inv(np.diag(np.diag(derivada_clarke(x))))@(e(x) - np.diag(derivada_clarke(x)@sem_diag_g(g)))
    return df


def nearest_correlation_matrix(x_input, g_input, iter = 1000, tol = 10**(-6)):
    """Algoritmo de Nearest Correlation Matrix"""
    iteracao = 1
    X_anterior = x_input
    X_atual = np.diag(atualiza_diag_x(X_anterior, g_input)) + sem_diag_g(g_input)

    while iteracao < iter:
        iteracao = iteracao + 1
        print("iteracao", iteracao - 1)
        print(derivada_clarke(X_anterior) @ X_atual)
        X_anterior = X_atual
        X_atual = np.diag(atualiza_diag_x(X_anterior, g_input)) + sem_diag_g(g_input)

        if np.linalg.norm(np.diag(derivada_clarke(X_atual) @ X_atual) - e(X_atual)) < tol:
            break      
        
    return derivada_clarke(X_anterior) @ X_atual, iteracao