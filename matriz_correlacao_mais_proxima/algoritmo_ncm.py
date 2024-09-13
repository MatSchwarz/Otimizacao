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
def SM_ncm(X_input,G_input,iter,tol):
    i = 1
    X_inicial = X_input
    X_proximo = Diag(Df(X_inicial,G_input)) + G_chapeu(G_input)

    while i < iter:
        i = i+1 
        print("iteracao",i-1)
        print(V(X_proximo) @ X_proximo)
        X_inicial = X_proximo
        X_proximo = Diag(Df(X_inicial,G_input)) + G_chapeu(G_input)

        if np.linalg.norm(np.diag(V(X_proximo) @ X_proximo) - e(X)) < tol:
            break
    
    return X_proximo, iter