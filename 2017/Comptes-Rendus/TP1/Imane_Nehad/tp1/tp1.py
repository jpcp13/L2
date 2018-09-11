from module_tp1 import *

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

#2.b

i=0
a=1.0
X=[]
for i in range(25):
	a=g(a) 
	print('valeur courante de a = {0}'.format(a))
	X.append(a)
print('')
#print X


#3.b.i

x0=1.0
epsi= 1e-12
x, cpt = point_fixe(g, x0, epsi)
print('test1 point_fixe :la racine de g par la methode du point fixe est de {0}, et on a fait {1} iterations'.format(x, cpt)) 
print('')

#3.b.ii

x0=-0.6
epsi=1e-12
v=point_fixe(g,x0,epsi)
print('test2 point_fixe :la racine de g par la methode du point fixe est de {0}'.format(v))
print('')	
	
#4.c.i

x0 = 1.0
epsi= 1e-12
x , cpt = newton(f, df, x0, epsi)
print('test 1 newton :la racine de f a {0} pres vaut r = {1}, et on a fait {2} iterations'.format(epsi, x, cpt))
print('')

#4.c.ii

x0 =-1.0
epsi= 1e-12
t = newton(f, df, x0, epsi)
print('test 2 newton :la racine de f a {0} pres vaut r = {1}'.format(epsi, t))
print('')

#5.b.i

x0, x1 = 1.5, 2.0
epsi= 1e-12
r = secante(f, x0, x1, epsi)

print('test 1 secante :la racine de f a {0} pres vaut r = {1}, et on a fait {2} iterations'.format(epsi, r, cpt))
print('')

#5.b.ii

x0, x1 = -1.0 , -0.5
epsi= 1e-12
r = secante(f, x0, x1, epsi)
print('test 2 secante :la racine de f a {0} pres vaut r = {1}'.format(epsi, r))
print('')

#6.b.i

xo , x1 = 1.5 , 2.0 
epsi= 1e-12
r= dichotomie(f, x0, x1 , epsi)
print('test 1 dichotomie :la racine de f a {0} pres vaut r = {1} , et on a fait {2} iterations'.format(epsi, r, cpt))
print('')

#6.b.ii

xo , x1 = 1.0 , 0.0 
epsi= 1e-12
r= dichotomie(f, x0, x1 , epsi)
print('test 2 dichotomie :la racine de f a {0} pres vaut r = {1}'.format(epsi, r))
print('')

