from func_auxiliares import *
import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg


def Newton_Semismooth(matriz_Q,vetor_q,x0,tol):
    matriz_T = T(matriz_Q)
    vetor_b = b(matriz_T,vetor_q).T
    x_depois = np.linalg.inv(Matriz_P(x0) + matriz_T)@vetor_b
    criterio_parar = np.linalg.norm(np.diag(Matriz_P(x_depois)) - 
                                    (np.diag(Matriz_P(x0))))
    x_antes = x_depois

    while criterio_parar > tol:
        x_depois =  np.linalg.inv(Matriz_P(x_antes) + matriz_T)@vetor_b
        criterio_parar = np.linalg.norm(np.diag(Matriz_P(x_depois)) - 
                                        (np.diag(Matriz_P(x_antes))))
        x_antes = x_depois

    return x_depois

