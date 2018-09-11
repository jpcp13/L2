import math
import numpy as np
import matplotlib.pyplot as plt
import time

################## Affichage d'un cercle #################
theta = np.linspace(0, 2*np.pi, 100)
x=np.cos(theta)
y=np.sin(theta)
plt.plot(x, y)
plt.grid()
compt=0
compt2=0
for i in range(1000):
    xpoint=2*np.random.rand()-1
    ypoint=2*np.random.rand()-1
    if (xpoint**2+ypoint**2)<1:
        plt.scatter(xpoint, ypoint, color='red', marker='.')
    else:
        plt.scatter(xpoint, ypoint, color='green', marker='.')
plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
plt.savefig('cercle.png')

def montecarlo_cercle(n):
    t=time.clock()
    compt=0
    for i in range(n):
        xpoint=2*np.random.rand()-1
        ypoint=2*np.random.rand()-1
        if (xpoint**2+ypoint**2)<1:
           compt=compt+1
    surface=(compt/float(n)*4)
    return surface, time.clock()-t

with open('monte_carlo_cercle.txt', 'w') as fichier2:
    fichier2.write('{0:6s} | {1:s} | {2:s}\n'.format('n', 'erreur', 'temps'))
    for i in range(6):
        surface, temps = montecarlo_cercle(10**i)
        fichier2.write('{0:6d} | {1:f} | {2:f}\n'.format(10**i, abs(surface-np.pi), temps))
