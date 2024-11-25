import numpy as np

def derivada_clarke(X): #Calcula a derivada generalizada de Clarke para a matriz X.

    eigv, u = np.linalg.eigh(X)  # Calcula os autovalores e autovetores de X
    
    Dii_pos = eigv > 0  # Devolve True autovalores positivos
    Dii_neg = eigv <= 0  # Devolve False para autovalores não positivos

    eigv[Dii_pos] = 1  # Modifica os valores True para 1
    eigv[Dii_neg] = 0  # Modifica os valores False para 0
    
    D = np.diag(eigv)  # Cria a matriz diagonal D com 1's ou 0's

    return u @ D @ u.T

def e(X): #Cria um vetor de uns com a mesma dimensão da diagonal principal de X.

    diagonal = np.diag(X)  # Extrai a diagonal principal de X
    return np.ones(diagonal.shape)  # Retorna um vetor de uns com a mesma dimensão da diagonal

def sem_diag_g(G):

    return G - np.diag(np.diag(G))  # Subtrai a diagonal principal de G
