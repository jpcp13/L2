# Definition des fonctions

def f(x):
    return x**2 - x - 1

def df(x):
    return 2*x - 1

def g(x):
    return 1 + 1/x

def h(x):
    return x - f(x)/df(x)

def point_fixe(g, x0, epsi): 
    delta = 2*epsi
    nbiter1=0
    while delta>epsi and nbiter1<150:
        nbiter1 += 1
        x1=g(x0)
        delta = abs(x1-x0)
        x0 = x1
    r = x0  
    return r, nbiter1

def newton(h,x0,epsi):
    delta = 2*epsi
    nbiter2 = 0
    while delta>epsi and nbiter2<150:
	nbiter2 += 1
        x1 = h(x0)
        delta = abs(x1 - x0)
        x0 = x1
    r = x0
    return r, nbiter2

def secante(f, x0, x1, epsi):
    delta = 2*epsi
    nbiter3=0
    while delta>epsi and nbiter3<150:
	nbiter3 += 1
        num = x1 - x0
        den = f(x1)-f(x0)
        x2 = x1 - (num/den)*f(x1)
        delta = abs(x2 - x1)
        x0=x1
        x1=x2
    t = x1
    return t, nbiter3
   
def dichotomie(f, a, b, epsi):
    g = a
    d = b
    nbiter4=0
    while (d-g) > 2*epsi and nbiter4<150:
    	nbiter4 = nbiter4+1
    	m = (d+g)/2
    	if ( f(g)*f(m)) <= 0 :
        	d=m
    	else : 
        	g = m
    
    return (d+g)/2 , nbiter4

# Listes de points de f(x)

x = -1 
X, Y, Points = [], [], []

while x < 3:
    
    point = (x, f(x)) 
    X.append(x) 
    Y.append(f(x)) 
    Points.append(point)
    x += 1
print("(x , f(x)) \n")
print(Points)

# Suite de g(x)

print("\nSuite g(x)\n")
x0 = 1.0
liste = [x0]
for i in range(25):
    x1 = g(x0)
    liste.append(x1)
    x0 = x1
    print(x0)

#Representation graphique

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1, 3, 0.3)
plt.plot(x, f(x),'r-',x,g(x),'b')
plt.grid('on')
plt.axis('equal')
plt.show()


#Tests

print("\nTest  Point fixe \n")
r,nbiter1=point_fixe(g,1.0,1e-15)
print "Nombre d'interation :",nbiter1
print "r :  ",r
print "g(r):",g(r)


print("\nTest Newton \n")
r1, nbiter2=newton( h, 1, 1e-15)
print "Nombre d'interation :",nbiter2
print "r :  ",r1
print "h(r):",h(r1)


print("\nTest Secante \n")
r2, nbiter3 =secante(f, 1.5, 2, 1e-15)
print "Nombre d'interation :",nbiter3
print "r :  ",r2
print "f(r):",f(r2)


print("\nTest dichotomie \n")
r3 , nbiter4 = dichotomie(f,1.5,2.0,1e-15)
print "Nombre d'interation :",nbiter4
print "r :  ",r3
print "f(r):",f(r3)




