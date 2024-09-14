import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg
from func_auxiliares_ncm import *


def diferencial_f(x,g):
    """Função responsável por fazer uma iteração do algoritmo"""
    df = np.linalg.inv(Diag(diag(V(x))))@(e(x) - diag(V(x)@G_chapeu(g)))
    return df


def sm_ncm(x_input,g_input,iter,tol):
    """Algoritmo de Nearest Correlation Matrix"""
    i = 1
    X_inicial = x_input
    X_proximo = Diag(diferencial_f(X_inicial,g_input)) + G_chapeu(g_input)

    while i < iter:
        i = i+1 
        print("iteracao",i-1)
        print(V(X_proximo) @ X_proximo)
        X_inicial = X_proximo
        X_proximo = Diag(diferencial_f(X_inicial,g_input)) + G_chapeu(g_input)

        if np.linalg.norm(np.diag(V(X_proximo) @ X_proximo) - e(X_proximo)) < tol:
            break
    
    return V(X_proximo) @ X_proximo, i