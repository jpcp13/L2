#(a) definition de f

import matplotlib.pyplot as plt
def f(x):
	return x**2 - x - 1


def df(x):
	return 2*x -1

x, dx = -1, 0.25
X, Y, points =[], [], []
while x <= 2:
	y = f(x)
	point = (x, y)
	X.append(x)
	Y.append(y)
	points.append(point)	
	x+=dx
print(' \nles absices sont: \n')
print(X)
print('\nles ordonnees sont: \n')
print(Y)
print('\nles coordonnees des points sont: \n')
print(points)
plt.plot(X, Y, 'b')
plt.grid()
plt.show()
print('\n')
def g(x):
	return 1 + 1/x

import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()

X=[]
x=1.0
for i in range (25):
	X.append(x)
	x=g(x)
print('\nLes 25 premieres Valeurs\n')
print(X)



def point_fixe(g, x0, e):
	nbiter=0
	delta= 2*e
	while delta > e:
		nbiter += 1
		x1=g(x0)
		delta=abs(x1-x0)
		x0=x1
	r = x0
	return r,nbiter
print('\npoint fixe avec x0 = 1.0 epsi = 10**(-12)\n')
x0=1.0
epsi=10**(-12)
r=point_fixe(g, x0, epsi)
print('r={0}\n'.format(r))
print('\npoint fixe avec x0 = -0.6 epsi = 10**(-12)\n')
x0=-0.6
epsi=10**(-12)
r=point_fixe(g, x0, epsi)
print('r={0}\n'.format(r))


def newton(f, df, x0, epsi):
	r= x0
	#stock = []
	i=1
	nbiter = 0


	while i == 1:
		nbiter += 1
		#stock.append(r)
		prec = r
		r = r - (f(r)/ df(r))
		if abs(r - prec) < epsi:
			i = 0
	return r,nbiter
print('\nnewton avec x0 = 1.0 epsi = 10**(-12)\n')
x0=1.0
epsi=10**(-12)
r=newton(f, df, x0, epsi)
print('r={0}\n'.format(r))


print('\nnewton avec x0 = -1.0 epsi = 10**(-12)\n')
x0=-1.0
epsi=10**(-12)
r=newton(f, df, x0, epsi)
print('r={0}\n'.format(r))


def secante(f, x0, x1, epsi):

	r= x0
	s= x1
#stock = []
	i=1
	nbiter = 0
	prec2 = r
	prec1 = s


	while i == 1:
		nbiter += 1
		#stock.append(r)


		r = prec1 - ((prec1-prec2)/(f(prec1)-f(prec2)))*f(prec1)

		prec2 = prec1
		prec1 = r

		#print(cpt)
		if abs(r - prec2) < epsi:
			i = 0
	return r,nbiter



def dichotomie(f, a, b, epsi):
#stock = []
	
	i=1
	nbiter = 0


	while i == 1:
		nbiter += 1
	#stock.append(r)
		if (f(a) >0 and f((a+b)/2)>0) or (f(a) < 0 and f((a+b)/2)< 0):
			a = (a+b)/2
		else:
			b = (a+b)/2
#print(cpt)
		if abs(b - a) < epsi:
			i = 0

	point = (a,b)
	return point




#verification du point fixe de g, solution de f
A, B = [], []
a, da = -1.0, 0.1
test=0

while a <= 2:
	b = g(a)
	A.append(a)
	B.append(b)
	a += da
	if (1+ 1/a) - a == 0:
		test = f(1+ 1/a)
print(test)


#(b) 25 premiers temes
print('\nles elements de la suite sont:\n')
res= 1.0
stock = []
i=0
print(res)


for i in range(25):
	stock.append(res)
	res= (1 + 1/res)
#print(stock)
# return res


#(c) On observe que la suite converge vers la racine positive de f




#Exo 3
#(a) la def de point_fixe probleme: la condition du if r 2 - prec 2 < epsi
#(b) test de point fixe


x0 = 1.0
epsi = 10**(-12)


r = point_fixe(g, x0, epsi)
print('r = {0}\n'.format(r))


x0 = -0.6
epsi = 1e-12
r = point_fixe(g, x0, epsi)
print('r = {0}\n'.format(r))


# Dans les 2 cas la suite converge bers le point fixe mais on remarque que pour le second cas on effectue plus d'operations que pour le premier.


# (c) dessin




#EXO 4
# (c) test , x0>0 => racine positive, et x0<0 racine negative
x0 = 2.0
epsi = 1e-12
r = newton(f, df, x0, epsi)
print('r={0}\n'.format(r))


x0 = -2.0
epsi = 1e-12
r = newton(f, df, x0, epsi)
print('r={0}\n'.format(r))






# EXO 5
#(b) test
print ('secante avec x0 = 1.5, x1 = 2.0 et epsi = 10e-12')
x0 = 1.5
x1 = 2.0
epsi = 1e-12
r = secante(f, x0, x1, epsi)
print('r={0}\n'.format(r))

print ('secante avec x0 = -1.0, x1 = 0.0 et epsi = 10e-12')
x0 = -1.0
x1 = 0.0
epsi = 1e-12
r = secante(f, x0, x1, epsi)
print('r={0}\n'.format(r))


# on remarque bien que la difference notoire par rapport a la methode de Newton est bien l'utilisation de la derivee.


#EXO 6

print ('dichotomie avec x0 = 1.5, x1 = 2.0 et epsi = 10e-12')
x0=1.5
x1=2.0
epsi=1e-12
r= dichotomie(f, a, b, epsi)
print('r={0}\n'.format(r))

print ('dichotomie avec x0 = -1.0, x1 = 0.0 et epsi = 10e-12')
x0=-1.0
x1=0.0
epsi=1e-12
r= dichotomie(f, a, b, epsi)
print('r={0}\n'.format(r))
