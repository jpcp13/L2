# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#******************************************************

from methods import *

#Partie 1 : x^2-x-1

#1.a)

def f(x):
    
   return x**2 - x - 1

x, dx = -1.0, 0.25
X, Y, Points = [], [], [] 

while x < 2:
    y = f(x)
    point = (x, y) 
    X.append(x) 
    Y.append(y)
    Points.append(point) 
    x += dx

print(X)
print(Y)
print("\n")

for point in Points:
   
    x = point[0] 
    y = point[1]
    if x >= 0.0: 
        print('{0:20.4f} {1:20.4f}'.format(x, y)) 
  
#1.b)    

print("\n")

import matplotlib.pyplot as plt 

plt.plot(X, Y, 'r')
plt.grid()
plt.savefig('1.png')



#1.c) Voir compte rendu 

#******************************************************

#Partie 2 : 1+1/x

#2.a)
def g(x):
	
	return 1+1/x

import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.savefig('2.png')


import numpy as np
t = np.arange(-2.0, -0.5, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.savefig('3.png')



#2.b)

x0=1.0
xn=[x0]
for i in range(25):
	x1=g(x0)
	xn.append(x1)
	x0=x1

print (x0)
print (xn)
print("\n")

#2.c) voir compte rendu

#******************************************************

#Partie 3 : Point Fixe

pt="*** Partie 3 : Point Fixe ***"
print(pt)
print('\n')

#3.a)
"""
migration de point_fixe vers module
"""

#3.b)


#Test 1
n= " Test 1 Point fixe"
print(n)
print("\n")
x0=1.0
epsi=10**-12

r= point_fixe(g,x0,epsi)
print("\n")

#Test 2
n=" Test 2 Point fixe"
print(n)
print("\n")
x0=-0.6
epsi=10**-12

r= point_fixe(g,x0,epsi)

print("\n")
#3.c)

#******************************************************

#Partie 4 : Newton

ne="**** Partie 4 : Newton ****"
print(ne)
print('\n')

#4.a)

d="Verification de g"
print(d)

x0=1.0
r= point_fixe(g,x0,epsi)
print('\n')
x0=-0.6
r= point_fixe(g,x0,epsi)

#4.b)
def df(x):
	return 2*x-1.0


#4.c)
"""
migration de newton vers module
"""
#Test 1
print("\n")
n=" Test 1 NEWTON"
print(n)
print("\n")

x0=1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print("\n")

#Test 2
n2=" Test 2 NEWTON"
print(n2)
print("\n")

x0=-1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print("\n")

#******************************************************

#Partie 5 : Secante

#5.a)

se="***** Partie 5 : Secante *****"
print(se)
print('\n')


#5.b)

#Test 1
print("\n")
si=" Test 1 Secante"
print(si)
print("\n")

x0=1.5
x1=2.0
epsi=1e-12
secante(f,x0,x1,epsi)
print("\n")

#Test 2
print("\n")
sa=" Test 2 Secante"
print(sa)
print("\n")

x0=-1.0
x1=-0.5
epsi=1e-12
secante(f,x0,x1,epsi)
print("\n")


#******************************************************

#Partie 6 : Dichotomie

di="****** Partie 6 : Dichotomie ******"
print(di)
print('\n')

# 6.a)
"""
migration de dichotomie vers module
"""
#6.b.i)

s="Test 1 Dichotomie"
print(s)
print("\n")

a=1.5
b=2.0
epsi=10**-12
r=dichotomie(f,a,b,epsi,0)
print('\n')

#6.b.ii)

t="Test 2 Dichotomie"
print(t)
print("\n")

a=-1.0
b=0.0
epsi=10**-12
r=dichotomie(f,a,b,epsi,0)
print('\n')

for i in range(5):
	a=1.5
	b=2.0
	epsi=10**-((i+1)*3)
	print((i+1)*3)
	r=dichotomie(f,a,b,epsi,0)
	print('\n')

#******************************************************
