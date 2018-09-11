from math import pi 
from tp3 import *

#a) voir fichier odt
#b) voir fichier tp3.py
#c) voir fichier tp3.py
#d)
u0 = 1.0
v0 = 0.0
U0 = np.array ([u0, v0])
T  = 4*pi
n  = 8000
tt, UU = euler_2(f5, U0 , T , n )
print tt
print UU

#e)
import matplotlib.pyplot as plt
plt.plot(tt, UU [0],'r-')
plt.plot(tt,UU[1],'b-') 
plt.plot( UU[0], UU[1], 'v-')
plt.grid('on')
plt.axis('equal')
plt.savefig('graphf5.png')
