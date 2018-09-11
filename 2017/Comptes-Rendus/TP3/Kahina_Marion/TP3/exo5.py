from module import *
from math import *
from time import clock
import numpy as np
import matplotlib.pyplot as plt

T = 4*pi
n = 100
U0 = np.array([1.0, 0.0])
tt, UU = euler2(F, U0, T, n)
plt.clf()
plt.plot(tt, UU[:, 0],'r',tt, UU[:, 1],'b',tt, UU[:, 0], 'v')
plt.grid()
plt.xlabel("temps")


tt,UU = euler2(F,U0, T, n)


#plt.show()
plt.savefig('graphe4.png')






