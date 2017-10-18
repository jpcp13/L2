#TD1:" IDOUFKER Aboubakr Benamara Taha

#Exo 1

import matplotlib.pyplot as plt 
def f(x) :
	return x**2 - x - 1.0
def df(x):
	return 2*x - 1.0
def g(x):
	return 1 + 1/x

def point_fixe(g, x0 ,eps ): 
	delta = 2*eps
	nbiter = 0
	while nbiter < 100 and delta > eps:
		nbiter = nbiter + 1
		x1 = g(x0)
		print ('point fixe de g(x) est {0:.15}'.format(x0))
		delta = abs(x1 - x0)
		x0 = x1
	print ('le compteur est a {1} et le point fixe vaut {0:.15f}'.format(x0, nbiter))
	return x0, nbiter


def newton(f, df, y0, epsi):
	y = y0 
	delta = 2*epsi
	cpt = 0
	while delta > epsi:
		cpt += 1
		y1 = y - f(y)/df(y)
		delta = abs(y1 - y)
		y = y1
		print ('la valeur approximative avec la fonction newton est {0} et le compteur est a {1}'.format(y, cpt))
	return y1

def secante(f, z0, z1, epsilon):
	z = z0
	delta = 2*epsilon
	i = 1
	nbiter2 = 0
	while i == 1:
		z = z1 - ((z1 - z0)*f(z1)/(f(z1) - f(z0)))
		delta = abs(z1 - z)
		z0 = z1
		z1 = z
		nbiter2 = nbiter2 + 1
		if delta < epsilon :
			i = 0
		print ('la valeur approximative avec la fonction secante est {0} et le compteur est a {1}'.format(z,nbiter2))
	return z

def dichotomie(f, a, b, epsi):
	delta = 2*epsi
	m = (a + b)/2
	nbiter3 = 0
	while delta > epsi:
		if (f(b)*f(a) < 0):
			if(f(a)*f(m) > 0):
				a = m
				print ('l encadrement approximatif avec la fonction dichotomie est {0},{1} et le compteur est a {2}'.format(m,b,nbiter3))
			if(f(b)*f(m) > 0):
				b = m
				print ('l encadrement approximatif avec la fonction dichotomie est {0},{1},et le compteur est a {2}'.format(a,m,nbiter3))
			else:
				c = 0
			m = (a + b)/2
		else:
			print ('impossible pas d encadrement')
		nbiter3 = nbiter3 + 1
		delta = abs(b-m)
	if(f(a)*f(m) > 0):
		return m,b,nbiter3
	if(f(a)*f(m) < 0):
		return a,m,nbiter3
		



x, dx = -1, 0.25
X, Y, Points = [], [], [] 


while x <= 2:
    y = f(x)
    point = (x, y) 
    X.append(x) 
    Y.append(y) 
    Points.append(point) 
    x += dx


plt.plot(X, Y, 'r')
plt.grid()
plt.show()

# Il y'a bien deux 0 aux coordonnees -0,6 et 1,6 
#Exo 2

# a 

def g(x):
	return 1 + 1/x
import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()

# D'apres la courbe ci-dessus, on a bien que les points fixes de g sont les 0 de f.

# b

X=[]
x = 1.0

for i in range(25):
	X.append(X)
	x = g(x)

for r in X:
    r = x
    print('{0:10.10f}'.format(r)) 

# c


#Exo3

x0 = 1.0
eps = 1e-15
x = point_fixe(g, x0, eps)

#exo 4
y0 = 1.0
epsi = 1e-15
y1 = newton(f, df, x0, epsi)

#exo 5
z0 = 1.5
z1 = 2
epsilon = 1e-15
z = secante(f, z0, z1, epsilon)

#exo 6
a = 1.5
b = 2.0
epsi = 1e-15
s = dichotomie(f, a, b, epsi)


