from module import *
from math import pi
import matplotlib.pyplot as plt


u0 = 1.0
v0 = 0.0
U0 = np.array([u0, v0])
T = 4*pi
n = 8000
tt, UU = euler_2(F, U0, T, n)
print tt
print UU

plt.plot(tt, UU [0],'b-')
plt.plot(tt, UU [1],'r-')
plt.plot(UU[0], UU[1],'v-')
plt.grid()
plt.axis('equal')
plt.savefig('graphf5.png')


