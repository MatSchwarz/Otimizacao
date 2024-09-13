import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg

#Essas funções não são necessárias, mas coloquei para melhor entendimento do
#que está ocorrendo no código
def diag(X): 
    return np.diag(X)

def Diag(vetor):
    return np.diag(vetor)


#Faz a decomposição espectral
def decomposição_espectral(X):
    if X.shape[0] != X.shape[1]:
        raise ValueError("matriz não quadrada")

    eigenvalues, eigenvectors = np.linalg.eigh(X)

    return eigenvalues, eigenvectors

#Calcula o valor da derivada generalizada de Clarke

def V(X):
    Lambda, U = decomposição_espectral(X)
    
    #Cria duas máscaras
    Dii_pos = Lambda > 0
    Dii_neg = Lambda <= 0  

    #faz a Matriz D
    Lambda[Dii_pos] = 1
    Lambda[Dii_neg] = 0
    D = Diag(Lambda)

    #cria a V(X)
    Vx = U@D@U.T

    return Vx

#Provavelmente tem um jeito bem mais eficiente de fazer isso

def e(X): 
    diagonal = diag(X) 
    e = np.ones(diagonal.shape)
    return e

#Implementa G^

def G_chapeu(G):
    G_chapeu = G - Diag(diag(G))
    return G_chapeu