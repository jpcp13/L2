#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock

def f(x):
        return sqrt(1 - x**2)
        
       
def point_milieu(f,a,b,n) : 
        x0 = a
        xx = [x0]
        for i in range (n+1):
                x1 = x0 + ((b-a)/n)
                xx.append(x1)
                x0 = x1
        


        cc = [] #creation d'une nouvelle liste vide
        for i in range (n+1):
                c = (xx[i] + xx[i+1])/2
                cc.append(c)
		t0=clock()

        ss = []
        for i in range(n) :
                s = ((b-a)/n)*f(cc[i+1])
                ss.append(s)
        t1=clock()
        S = 0
        for i in range(n) :
                S += ss[i]  

	I = (sqrt(3)/4) + (pi/6)
	print('\n')

	A = abs(S-I)
	print('Erreur commise : ')
	print(A)
	print('\n')

	t2 = t1 - t0
	print('Le temps de calcul de l integrale est :')
	print(t2)
	print('\n')

        return S


#EXERCICE 1

#1B.

x, dx = -0.5, 0.1
X, Y, Points = [], [], []


while x < 0.5:
        y = f(x)
        point = (x, y)

        X.append(x) 
        Y.append(y) 
        Points.append(point) 
        x += dx
print('\n')

import matplotlib.pyplot as plt
plt.plot(X, Y, '*r')
plt.grid()
#plt.show()
#plt.savefig('fig2.png') 

#1C.

#a voir

#EXERCICE 2

#2A.

#Rendu papier

#2B.

x0 = -0.5
xx = [x0]
for i in range (5):
        x1 = x0 + 0.25
        xx.append(x1)
        x0 = x1
        
print(x0)
print(xx)
print('\n')


cc = [] #creation d'une nouvelle liste vide
for i in range (5):
        c = (xx[i] + xx[i+1])/2
        cc.append(c)
        
print(cc)

t0 = clock ()

print('\n')

#2C.

ss = []
for i in range(4) :
        s = 0.25*f(cc[i+1])
        ss.append(s)
#print(ss)   
#print('\n')

t1 = clock ()

S = ss[0] + ss[1]  + ss[2] + ss[3]  
print('Somme de la surface') 
print(S) 
I = (sqrt(3)/4) + (pi/6)
print('\n')

A = abs(S-I)
print('Erreur commise : ')
print(A)
print('\n')

#2D.

t2 = t1 - t0
print('Le temps de calcul de l integrale est :')
print(t2)
print('\n')

#2F.
print('Test 1') 
a = -0.5
b = 0.5
n = 10
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

print('Test 2') 
a = -0.5
b = 0.5
n = 100
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

print('Test 3') 
a = -0.5
b = 0.5
n = 1000
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

print('Test 4') 
a = -0.5
b = 0.5
n = 10000
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

print('Test 5') 
a = -0.5
b = 0.5
n = 100000
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

print('Test 6') 
a = -0.5
b = 0.5
n = 1000000
r = point_milieu(f, a, b, n)
print('point milieu')
print(r)
print('\n')

