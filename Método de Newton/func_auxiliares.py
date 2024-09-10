import pandas as pd
import numpy as np
import scipy.stats
from scipy import linalg

def T(Q):
    T = np.linalg.inv((Q - np.identity(len(Q))))
    return T

def b(T,q):
    b = T@q
    return b

def proj_ortante(x):
    proj_x = np.maximum(x, 0)
    return proj_x

def Matriz_P(x):
    p = proj_ortante(x)
    p = np.sign(p)
    P = np.diag(p)
    return P