from math import *
from time import clock
import numpy as np
import matplotlib.pyplot as plt
from fonction import* 

def u(t):
    return np.exp(-t)

def f(t , u):
    return -u

def f1(t , u):
    return -u + t

def f2(t , u):
    return u**2

def f3(t , u):
    return u**2 - t


#fonction f

u0 = 1.0
T=2.0
n=10
tt = np.linspace(0, T, n+1)
uu = np.zeros(n+1)

tt, uu = euler(f, u0, T, n)

#fonction f1

u0 = 1.0
T = 2.0
n = 10
tt1 = np.linspace(0, T, n+1)
uu1 = np.zeros(n+1)

tt1, uu1 = euler(f1, u0, T, n)



#fonction f2 assymptote apres 1.1 car les resultats explosent

u0 = 1.0
T = 1.1
n = 10
tt2 = np.linspace(0, T, n+1)
uu2 = np.zeros(n+1)

tt2, uu2 = euler(f2, u0, T, n)


#fonction f3 1.1 est deja trop grande pour converger. a 1.1 ca converge vers 9,5

u0 = 1.0
T=1.0
n=10000
tt3 = np.linspace(0, T, n+1)
uu3 = np.zeros(n+1)

tt3, uu3 = euler(f3, u0, T, n)












