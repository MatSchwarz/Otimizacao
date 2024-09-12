import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg
from func_auxiliaresNCM import *

#Função responsável por fazer uma iteração do algoritmo

def Df(X,G):
    Df = np.linalg.inv(Diag(diag(V(X))))@(e(X) - diag(V(X)@G_chapeu(G)))
    return Df

