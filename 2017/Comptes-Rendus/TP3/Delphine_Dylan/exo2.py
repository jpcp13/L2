import numpy as np
import matplotlib.pyplot as plt
from math import *
from moduletp3 import *

def u(t):
	return np.exp(-t)

u0=1.0
T=10.0
n=80
h = T/n
tt = np.linspace(0, T,n)
uu = np.zeros(n)
uu[0] = u0

for i in range(1, n):
	u1 = u0 - h*u0
	uu[i] = u1
	u0 = u1

plt.clf()
plt.plot(tt, u(tt), '-r', tt, uu, '+k')
plt.grid()
plt.savefig('Graphique.png') 
