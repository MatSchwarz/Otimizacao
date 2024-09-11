from func_auxiliares import *
import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg


def Newton_Semismooth(Q,q,x0,tol):
    matriz_T = T(Q)
    vetor_b = b(matriz_T,q).T
    x_depois =  np.array((np.linalg.inv(Matriz_P(x0) + matriz_T)@vetor_b).T)[0]
    criterio_parar = np.linalg.norm(np.diag(Matriz_P(x_depois)) - (np.diag(Matriz_P(x0))))
    x_antes = x_depois

    while criterio_parar > tol:
        x_depois =  np.array((np.linalg.inv(Matriz_P(x_antes) + matriz_T)@vetor_b).T)[0]
        x_antes = x_depois
        criterio_parar = np.linalg.norm(np.diag(Matriz_P(x_depois)) - (np.diag(Matriz_P(x_antes))))

    return x_depois