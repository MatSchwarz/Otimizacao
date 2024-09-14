import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg
from func_auxiliares_ncm import *

#Função responsável por fazer uma iteração do algoritmo

def Df(X,G):
    Df = np.linalg.inv(Diag(diag(V(X))))@(e(X) - diag(V(X)@G_chapeu(G)))
    return Df


#Algoritmo de Nearest Correlation Matrix
def sm_ncm(x_input,g_input,iter,tol):
    i = 1
    X_inicial = x_input
    X_proximo = Diag(Df(X_inicial,g_input)) + G_chapeu(g_input)

    while i < iter:
        i = i+1 
        print("iteracao",i-1)
        print(V(X_proximo) @ X_proximo)
        X_inicial = X_proximo
        X_proximo = Diag(Df(X_inicial,g_input)) + G_chapeu(g_input)

        if np.linalg.norm(np.diag(V(X_proximo) @ X_proximo) - e(X_proximo)) < tol:
            break
    
    return X_proximo, iter