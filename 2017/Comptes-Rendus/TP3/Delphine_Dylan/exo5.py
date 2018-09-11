import numpy as np
import matplotlib.pyplot as plt
from math import pi
from moduletp3 import *




u0=1.0
v0= 0.0
U0 = np.array([u0, v0])
U = U0
T = 6*pi
n = 10000

#a


#b
t = np.linspace(0.0, 2.0, 100)
U_out = F(t, U)
print b
#c
	

tt, UU = euler2(F, U0, T, n)


plt.clf()
plt.plot(tt,UU [0], 'b', tt,UU [1], 'r')
plt.grid()
plt.axis('equal')
plt.savefig('graphF1.png')

plt.clf()
plt.plot(UU [0], UU [1], 'k', marker='.', markersize=0.8)
plt.grid()
plt.axis('equal')
plt.savefig('graphF2.png')



