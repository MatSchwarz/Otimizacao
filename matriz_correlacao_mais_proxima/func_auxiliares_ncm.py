import numpy as np

#Calcula o valor da derivada generalizada de Clarke
def derivada_clarke(X):
    
    #Calcula os autovalores e autovetores
    eigv, u = np.linalg.eigh(X)
    
    #Cria duas máscaras
    Dii_pos = eigv > 0
    Dii_neg = eigv <= 0 

    #faz a Matriz D
    eigv[Dii_pos] = 1
    eigv[Dii_neg] = 0
    D = np.diag(eigv)

    #cria a V(X)
    derivada_clarke = u@D@u.T

    return derivada_clarke

#implementa um vetor de uns da mesma dimensão da diagonal da diagonal principal de X

def e(X): 
    diagonal = np.diag(X) 
    e = np.ones(diagonal.shape)
    return e

#Implementa G sem diagonal principal

def sem_diag_g(G):
    sem_diag_g = G - np.diag(np.diag(G))
    return sem_diag_g