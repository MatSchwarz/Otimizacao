import numpy as np

def projecao_S(R):
    # Implementa a projeção no subconjunto semidefinido
    # Implementação de espaço reservado, substitua pela lógica de projeção real
    eigvals, eigvecs = np.linalg.eigh(R)
    eigvals[eigvals < 0] = 0
    return eigvecs @ np.diag(eigvals) @ eigvecs.T

def projecao_U(Y):
    # Implementa a projeção no subconjunto de diagonal unitária
    # Implementação de espaço reservado, substitua pela lógica de projeção real
    np.fill_diagonal(Y, 1)
    return Y

def projecoes_alternadas(G, max_iteracoes=1000):

    delta_S = np.zeros_like(G)
    X = G.copy()

    X_anterior = X.copy()
    
    for k in range(1, max_iteracoes + 1):
        

        R = X - delta_S
        
        # Projeta no subconjunto semidefinido
        Y = projecao_S(R)
        
        delta_S = Y - R
        
        # Projeta no subconjunto de diagonal unitária
        X = projecao_U(Y)
        
        # Critério de parada
        if np.linalg.norm(X - X_anterior) / np.linalg.norm(X) < 1e-6:
            break
        
        X_anterior = X.copy()
    return X
