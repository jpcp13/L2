def f(x):
	return x**2 - x - 1

def df(x):
    return 2*x -1

def g(x):
	return 1 + 1.0/x


def point_fixe(g, x0, epsi):
	x = x0
	delta = 2*epsi
	nbiter = 0

	while delta > epsi:
		nbiter += 1
		x1=g(x)
		delta = abs(x1 - x)
		x = x1
		#print x
	
	return x, nbiter

def newton(f, df, x0, epsi):
	r= x0
	i=1
	nbiter = 0

	while i == 1:
		nbiter += 1
		aux = r
		r = r - (f(r)/ df(r))
		if abs(r - aux) < epsi:
			i = 0   
	return r, nbiter

def secante(f, x0, x1, epsi):
	r= x0
	s= x1
	i=1
	aux2 = r
	aux1 = s
	nbiter = 0

	while i == 1:
		nbiter += 1
		r = aux1 - ((aux1-aux2)/(f(aux1)-f(aux2)))*f(aux1)
		aux2 = aux1
		aux1 = r
		if abs(r - aux2) < epsi:
			i = 0   
	return r, nbiter

def dichotomie(f, a, b, epsi):  
	i=1
	nbiter = 0

	while i == 1:
		nbiter += 1
		if (f(a) >0 and f((a+b)/2)>0) or (f(a) < 0 and f((a+b)/2)< 0):
			a = (a+b)/2
		else: 
			b = (a+b)/2
		if abs(b - a) < epsi:
			i = 0   
            
	point = (a,b)
	return point, nbiter


############################# start 
"""
#EXO1
x = -1
X, Y, Points = [], [], [] 

while x <= 2:
	y = f(x)
	point = (x, y)
	X.append(x)
	Y.append(y)
	Points.append(point) 
	x += 0.01

#print(X)
#print(Y)
#print(Points)

import matplotlib.pyplot as plt
plt.plot(X, Y, 'r')
plt.grid()
plt.show()



x0 = 1.5
i = 0
steak = []

print (x0)

for i in range(20):
	steak.append(x0)
	x0 = (1 + 1/x0)
	print (x0)


import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()

#Les 25 premiers termes

print("Les 25 premiers termes sont :")

res=1.0
stock=[ ]
i=0
print(res)

for i in range(25):
	stock.append(res)
	res=(1+1/res)
	print(res)

"""


#EXO 3
print('')
print('METHODE DU POINT FIXE')
print('')
x0 = 1.0
epsi = 1e-12

r, nbiter = point_fixe(g, x0, epsi)
print('r = {0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))

x0 = -0.6
epsi = 1e-12

r, nbiter = point_fixe(g, x0, epsi)
print('r = {0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))
print('')

#EXO 4
print('')
print('METHODE DE NEWTON')
print('')
x0 = 1.0
epsi = 1e-12
r, nbiter = newton(f, df, x0, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))

x0 = -1.0
epsi = 1e-12
r, nbiter = newton(f, df, x0, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))
print('')

#EXO 5
print('')
print('METHODE DE LA SECANTE')
print('')
x0 = 1.5
x1 = 2.0
epsi = 1e-12
r, nbiter = secante(f, x0, x1, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))


x0 = -1.0
x1 = 0.0
epsi = 1e-12
r, nbiter = secante(f, x0, x1, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))
print('')

#EXO 6
print('')
print('METHODE DE DICHOTOMIE')
print('')
a=1.5
b=2.0
epsi=1e-12
r, nbiter = dichotomie(f, a, b, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))


a=-1.0
b=0.0
epsi=1e-12
r, nbiter = dichotomie(f, a, b, epsi)
print('r={0} et mon nombre d\'iterations vaut {1}'.format(r, nbiter))
























