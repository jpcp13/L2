# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#******************************************************

#Partie1 

import time

def f(x):
	from math import sqrt
	return sqrt(1-x**2)

x, dx = -0.5, 0.01
X, Y, Points = [], [], [] 

while x < 0.5:
   	y = f(x)
    	point = (x, y) 
    	X.append(x) 
    	Y.append(y)
    	Points.append(point) 
    	x += dx


for point in Points:
   
    x = point[0] 
    y = point[1]
    if x >= 0.0: 
        print('{0:20.4f} {1:20.4f}'.format(x, y)) 



import matplotlib.pyplot as plt 
plt.plot(X, Y, 'r')
plt.grid()
plt.show()


#*********************************************************

#Partie2

t0=time.clock()
x0=-0.5
xx=[x0] # Ceci enregistre les points xi de la subdivision dans une liste
for i in range(4):
	x1= x0 + 0.25
	xx.append(x1)
	x0=x1

cc = [] # Ceci enregistre les milieux de ces sous intervalles dans une liste
for i in range(4):
	c=(xx[i]+xx[i+1])/2
	cc.append(c)
#pour le calcul de surface

s=0
for i in range(4):

	s = s + (xx[i+1]-xx[i])*f(cc[i])
	
t1=time.clock()

print('Les points:')
print(xx)   
print('\n')

print('Les milieux :')
print(cc)
print('\n')

print('La somme de la surface :')
print(s)
print('\n')

print"Le temps de calcul est:"
t=t1-t0
print(t)
print('\n')

print('L\'integrale I:')
import math
from math import sqrt
I= math.pi/6 + sqrt(3)/4
print(I)
print('\n')

r=abs(s-I)
print('erreur commise:')
print(r)
print('\n')


n="n"
d="erreur"
t="temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))
t="---------------------------------------------"
print(t)
for i in range(6):

    t5=time.clock()
    p= point_milieu(f,-0.5,0.5,10**(i+1))
    t6=time.clock()
    r=abs(p-I)
    y=t6-t5
    print('{0:10} | {1:17} | {2:10}'.format(10**(i+1),r,y))
  
	#METHODE DE TRAPÈZE
n="n"
d="erreur"
t="temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))
t="---------------------------------------------"
print(t)

for i in range(6):
    t5=time.clock()
    p= trapezes(f,-0.5,0.5,10**(i+1))
    t6=time.clock()
    r=abs(p-I)
    y=t6-t5
    print('{0:10} | {1:17} | {2:10}'.format(10**(i+1),r,y))


    #METHODE DE SIMPSON
n="n"
d="erreur"
t="temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))
t="---------------------------------------------"
print(t)

for i in range(6):
    t5=time.clock()
    p= Simpson(f,-0.5,0.5,10**(i+1))
    t6=time.clock()
    r=abs(p-I)
    y=t6-t5
    print('{0:10} | {1:13} | {2:10}'.format(10**(i+1),r,y))

print('\n')

