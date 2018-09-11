#SABABADY KAMALA
#SELVARAJAH DINUSAN


import math
from tp3 import *


u0 = 1.0
v0 = 0.0
U0 = np.array([u0,v0])
T = 4*math.pi
n = 8000
tt, UU = euler(f5, U0 ,T, n)

import matplotlib.pyplot as plt

plt.plot(tt, UU[0],'b-')
plt.plot(tt, UU[1],'r-')
plt.plot(UU[0], UU[1],'v-')
plt.axis("equal")
plt.grid()
plt.savefig('5.png')


