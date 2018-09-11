import matplotlib.pyplot as plt
import numpy as np
from math import *
from pylab import *
from methods import euler

def U(u,v):
	return np.array([u,v])



def F(t,U):
	#u0 = U[0]
	#v0 = 
	#return u0* cos(t) + v0 * sin(t)
	return np.array([U[1],-U[0]])

def Euler(F,U0,T,n):
	h = float (T)/n
	
	tt = np.linspace(0,T,n+1)
	suite = [U0]
	for i in range(0,n):
		U0 = U0 + h*F(h*i,U0)
		suite.append(U0)
	UU = np.asarray(suite) #convertir une liste en array
	return tt,UU
N=1000

tt,UU = Euler(F,U(1,0),4*np.pi,N)
x = np.linspace(0, 4*np.pi,100)
y=np.cos(x)
y2=-np.sin(x)
y3 = -np.sin(np.arccos(x))

print tt,UU


plt.title('u en fonction du temps')
plt.plot(x, y, color = 'green')
plt.scatter(tt, [UU[i][0] for i in range(N+1)], color='red', marker='.')

plt.show()


plt.title('v en fonction du temps')
plt.plot(x, y2, color = 'green')
plt.scatter(tt, [UU[j][1] for j in range(N+1)], color='red', marker='.')
plt.show()

plt.title('v en fonction de u')
plt.plot(x, y3, color = 'green')
plt.scatter(tt, [UU[j][1] for j in range(N+1)], color='red', marker='.')
plt.show()
