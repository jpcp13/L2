from tp3_fonction import *
import matplotlib.pyplot as plt
from numpy import *
from math import *
from pylab import *

def f(x,u):
	return -u
def u(x):
	return exp(-x)

## exo 1 

X, Y, Points = [], [], []
x=0
dx=0.25
while x <= 2.5:
	y = u(x)
	point = (x, y) 
	X.append(x)  
	Y.append(y) 
	Points.append(point) 
	x += dx

print(X)
print(Y)


##exercice 2

T = 2.0
n =  10
h = float(T)/n



X, U =[ ], []
u0=1
x0=0

ui=u0
xi=x0

X.append(x0)
U.append(u0)

for i in range (0,n):
	xi = xi +h
	ui += h*f(xi,ui)
	X.append(xi)
	U.append(ui)
print(X)
print(U)

plt.clf()
plt.plot(X, U, 'b') 
'''tracer deux courbe sur le meme graphe alors qu'on savez pas le faire avant contre rendu'''

plt.grid()
plt.savefig('graphe(1).png')

#exercice 4 b	
euler(f,1,2.0,10)

# exercice 5 b)
def F(t, U):
	w=1.0
	u=U[0]
	v=U[1]
	Up=np.zeros(2)
	Up[0]=v
	Up[1]=-(w**2)*u
	return Up
# exercice 5 d)
T = 4*pi
n = 100
U0 = np.array([1.0, 0.0])
tt, UU = euler2(F, U0, T, n)
plt.clf()
plt.plot(tt, UU[:, 0],'r',tt, UU[:, 1],'b')
plt.grid()
plt.xlabel("temps")
plt.savefig('graphe5.png')

plt.clf()
plt.plot(UU[:, 0], UU[:, 1],'r')
plt.grid()
plt.savefig('graphe6.png')



