from module import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

u0 = 1.0
T=2.0
n=10
h=T/n
tt = np.linspace(0, T, n+1)
uu = np.zeros(n+1)
uu[0] = u0

for i in range(1, n+1):
	u1 = u0 - h*u0
	uu[i] = u1
	u0 = u1
	print(uu[i])

plt.clf()
plt.grid()
plt.plot(tt, u(tt), '*r', tt, uu, '.k')
plt.savefig('CourbeU.png')

plt.clf()
plt.grid()
plt.plot(tt, u(tt) - uu, '*g') #courbe de l'erreur
plt.savefig('erreur_exo2.png')
