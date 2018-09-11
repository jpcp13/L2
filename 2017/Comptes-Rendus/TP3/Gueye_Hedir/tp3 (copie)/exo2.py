#Mouhamadou Moustapha Gueye
#Lynda Hedir

import matplotlib.pyplot as plt
from methodes import *

T = 2.0
n = 10
h = T/n
t0 = 0
tt = np.zeros(n+1)

for i in range (n+1):
	tt[i] = i * h

uu = np.zeros(n+1)
u0 = 1.0
uu[0] = u0
for i in range (1,n+1):
	u1 = u0 + h * f(tt[i-1],u0)
	uu[i] = u1
	u0 = u1
x = np.linspace(0, 2, 100)
plt.plot(x, np.exp(-x),'b-')
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid()
plt.savefig('2.png')

plt.plot(tt, uu,'r.')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f=exp(-x)","u'(t)=-u(t)"])
plt.axis("equal")
plt.grid()
plt.savefig('2.png')
