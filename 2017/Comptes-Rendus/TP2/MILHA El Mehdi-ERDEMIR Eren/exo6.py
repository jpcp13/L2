import math 
from numpy import *
import matplotlib.pyplot as plt
import time 
import numpy as np


#a.Cercle

theta = np.linspace(0,2*np.pi, 100)
Xcercle = np.cos(theta)
Ycercle = np.sin(theta)
plt.plot(Xcercle, Ycercle)
plt.axis("equal")
plt.show()
plt.savefig('cercle.png')

#b.
print('\n')
import numpy.random as npr
print('Quelques valeurs aleatoires entre -1 et 1:')
print(npr.uniform(-1,1,10))

#c.
for i in range(100):
    xpoint=2*np.random.rand()-1
    ypoint=2*np.random.rand()-1
    if (xpoint**2+ypoint**2)<1:
        plt.scatter(xpoint, ypoint, color='red',marker='.')
    else:
        plt.scatter(xpoint, ypoint, color='green',marker='.')

plt.xlim(-1.25, 1.25)
plt.savefig('cercle1.png')

plt.xlim(-1.25, 1.25)

def montecarlo(N):
    t=time.clock()
    cmpt=0
    for i in range(N):
        xpoint = 2*np.random.rand()-1
        ypoint =2*np.random.rand()-1
        if (xpoint**2+ypoint**2)<1:
            plt.scatter(xpoint, ypoint, color='red', marker='.')
            cmpt= cmpt +1
    S= (cmpt/float(N)*4)
    return S, time.clock()-t

#montecarlo
m_c, cmpt= montecarlo(10000)
print('2eme test montecarlo = {0} et le temps {1}'.format(m_c, cmpt))
