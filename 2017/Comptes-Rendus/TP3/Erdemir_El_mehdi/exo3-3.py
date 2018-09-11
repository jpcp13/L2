import numpy as np
from math import *
from time import clock

def u(t):
    return np.exp(-t)

def f(t, u):
    return -u

def euler(f,u0,T,n):
    t0 = 0.0
    h = T/n
    tt = np.zeros(n+1)
    uu = np.zeros(n+1)
    uu[0] = u0
    tt[0] = t0
    for k in range(1,n+1):
        u1 = u0 + h*f(t0,u0)
        uu[k] = u1
        t1 = t0 + h
        tt[k] = t1
        u0 = u1
        t0 = t1
    return tt,uu



