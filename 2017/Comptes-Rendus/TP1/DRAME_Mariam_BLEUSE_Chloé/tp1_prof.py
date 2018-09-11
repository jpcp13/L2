def f(x):
	y = x**2-x-1.0
	return y

def df(x):
	y=2*x-1
	return y

def g(x):
	y = 1 + 1.0/x
	return y

def point_fixe(g, x0, epsi):
	x = x0 # x joue le role de x_n
	delta = 2*epsi
	while delta > epsi:
		x1 = g(x) # x1 joue le role de x_{n+1}
		delta = abs(x1 - x)
		x = x1
	return x

def h(x):
	y=x-(f(x)/(2*x-1))
	return y

def newton(f, df, x0, epsi):
	cpt = 0
	x=x0
	delta=2*epsi
	while delta>epsi:
		cpt = cpt + 1
		v=x-f(x)/df(x)
		delta=abs(x-v)
		x=v
	return v, cpt

def secante(f, x0, x1, epsi):
	#x0 va jouer le role de xn-1
	#x1 va jouer le role de xn
	delta=2*epsi
	cpt = 0
	while delta>epsi and cpt < 100:
		cpt += 1
		num = x1 - x0
		delta = abs(num)
		den = f(x1) - f(x0)
		x2 = x1 - num/den*f(x1)
		x0 = x1
		x1 = x2
	return x2, cpt
	
def dichotomie(f, a, b, epsi):
	cpt = 0
	if b-a<=epsi:
		cpt += 1
		return a,b,cpt
	else:
		c=(a+b)/2
		if f(a)*f(c)<=0:
			cpt += 1
			return dichotomie(f,a,c,epsi),cpt		
		else:
			cpt += 1
			return dichotomie(f,c,b,epsi),cpt


###################################""""""" debut programme
"""
x0 = -1.0
x1 = -0.5
epsi = 1e-12

r = secante(f, x0, x1, epsi)
print r


#Exo 1
#a) voir ci dessus la fonction f
#b) 
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-1.0, 2.0, 0.1)
y = f(x)
plt.plot(x, y)
plt.show()

"""
#Exo2

x=1.0
X=[]
for k in range(0,25):
	X.append(g(x))
	x=g(x)
print X

"""

#Exo3
 #test 1
x0 = 1.0
epsi = 1e-12
r, cpt = point_fixe(h, x0, epsi)
print ('la racine vaut approximativement {0}, et on a fait {1} iterations'.format(r, cpt))
print g(r)


#test 2
x0 = -0.6
epsi = 1e-12
r = point_fixe(g, x0, epsi)
print r
print g(r)

#cela converge vers la racine posite, et on s'attendait a une convergence vers la racine -0.618

 #Exo 4
#a
x0 = 1.0
epsi = 1e-12
r = point_fixe(h, x0, epsi)
print r
print h(r)


#b
x0=-1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print r
"
#exo6

#test1
a=1.5
b=2.0
epsi=1e-12
r, cpt=dichotomie(f, a, b, epsi)
print ('la racine vaut approximativement {0}, et on a fait {1} iterations'.format(r, cpt))


#test2
a=-1.0
b=0.0
epsi=1e-12
r=dichotomie(f,a,b,epsi)
print r
"""
