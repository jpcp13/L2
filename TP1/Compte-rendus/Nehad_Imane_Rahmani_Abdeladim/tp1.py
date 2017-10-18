
#1.a
def f(x):
	return x**2 -x-1.0

def df(x):
	return 2*x - 1.0
'''
#1.b
x, dx = -1.0, 0.25
X, Y, Points = [], [], []

while x <= 2:
    y = f(x)
    point = (x, y) 
    X.append(x) 
    Y.append(y) 
    Points.append(point) 
    x += dx

import matplotlib.pyplot as plt 
plt.plot(X, Y, 'r')
plt.grid()
plt.show()
#2.a
'''
def g(x):
	return 1 + 1/x
#2.b
'''
i=0
a=1.0
X=[]
for i in range(25):
	a=g(a) 
	print('valeur courante de a = {0}'.format(a))
	X.append(a)
#print X
'''
#3.a
def point_fixe(g, x0, epsi):
	x=x0
	delta = 2*epsi
	cpt = 0
	while delta > epsi:
		x1=g(x)
		delta = abs(x1-x)
		x=x1
		cpt+= 1
	return x, cpt
#3.b.i

x0=1.0
epsi= 1e-12
x, cpt = point_fixe(g, x0, epsi)
print('test1 point_fixe :la racine de g par la methode du point fixe est de {0}, et on a fait {1} iterations'.format(x, cpt)) 


#3.b.ii

x0=-0.6
epsi=1e-12
v=point_fixe(g,x0,epsi)
print('test2 point_fixe :la racine de g par la methode du point fixe est de {0}'.format(v))


#4.b
def newton(f, df, x0, epsi):
	x = x0
	delta = 2*epsi
	cpt = 0
	while delta > epsi:
		x1 = x - f(x)/df(x) # x est la valeur courante (equivalent a x_n), x1 est la valeur suivante (equivalent a x_n+1)
		delta = abs(x1-x)
		x = x1
		cpt+= 1
	return x , cpt	

#4.c.i

x0 = 1.0
epsi= 1e-12
x , cpt = newton(f, df, x0, epsi)
print('test 1 newton :la racine de f a {0} pres vaut r = {1}, et on a fait {2} iterations'.format(epsi, x, cpt))

#4.c.ii

x0 =-1.0
epsi= 1e-12
x = newton(f, df, x0, epsi)
print('test 2 newton :la racine de f a {0} pres vaut r = {1}'.format(epsi, x))



#5.a
def secante(f, x0, x1, epsi):
	delta = 2*epsi
	c=0
	cpt= 0
	while delta > epsi and c < 100:
		# x0 va representer x_{n-1}, x1 va representer x_n, x2 va representer x_{n+1} dans la recurrence donnee par l'enonce.
		
		y0, y1 = f(x0), f(x1)
		
		#print('denominator =', y1 - y0)
		#nous avons fait ce test pour savoir a partir de quel moment le denominateur est considere comme nul
		
		x2 = x1 - (x1-x0)/(y1 - y0) * f(x1)
		delta = abs(x2-x1)
		# je mests a jour x0, x1
		x0, x1 = x1, x2 # syntaxe python; en C, on aurait ecrit deux lignes.
		c+=1
		cpt+= 1 
	return x2 ,cpt

#5.b.i

x0, x1 = 1.5, 2.0
epsi= 1e-12
x , cpt= secante(f, x0, x1, epsi)
#erreur = f(x)
#print('l"erreur est {0}'. format(erreur))
print('test 1 secante :la racine de f a {0} pres vaut r = {1}, et on a fait {2} iterations'.format(epsi, x, cpt))

#5.b.ii

x0, x1 = -1.0 , -0.5
epsi= 1e-12
r = secante(f, x0, x1, epsi)
print('test 2 secante :la racine de f a {0} pres vaut r = {1}'.format(epsi, r))

#6.a

def dichotomie(f, x0, x1, epsi):
	delta= 2*epsi
	c=0
	cpt= 0
	#on rajoute un compteur pour eviter d'avoir une boucle a l'infinie
	while delta > epsi and c < 100 :
		if (f(x0) >0 and f((x0+x1)/2)>0) or (f(x0) < 0 and f((x0+x1)/2)< 0):
			x0 = (x0+x1)/2
		else: 
			x1 = (x0+x1)/2
			delta = abs(x1-x0)
			
		c+= 1
		cpt += 1
	return x1 , cpt

#6.b.i

x0 , x1 = 1.5 , 2.0 
epsi= 1e-12
r, cpt= dichotomie(f, x0, x1 , epsi)
print('test 1 dichotomie :la racine de f a {0} pres vaut r = {1} , et on a fait {2} iterations'.format(epsi, r, cpt))

#6.b.ii

xo , x1 = 1.0 , 0.0 
epsi= 1e-12
r= dichotomie(f, x0, x1 , epsi)
print('test 2 dichotomie :la racine de f a {0} pres vaut r = {1}'.format(epsi, r))


