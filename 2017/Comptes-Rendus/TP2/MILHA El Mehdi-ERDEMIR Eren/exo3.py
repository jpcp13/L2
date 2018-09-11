import matplotlib.pyplot as plt
#matplotlib.pyplot

from math import *

def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a=-0.5
b=0.5

def trapezes(f,a,b,n) :
    h=float(b-a) / n
    s=0.0
    s += f(a)/2.0
    for i in range(1,n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h


print('_n')
for i in range (1,7):
    n=10
    t=trapezes(f , a, b, n**i)
    print('\n')
    print('{0}eme test trapezes = {1} ' .format(i,t))



