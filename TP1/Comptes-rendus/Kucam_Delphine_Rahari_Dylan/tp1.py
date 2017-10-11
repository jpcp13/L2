

def f(x) :
	return x**2 - x - 1

def g(x) :
	return 1 + (1/x)


def point_fixe(g, x0, epsi) :
	x = x0 # x joue le role de x_n
	delta = 2*epsi
	nbiter = 0
	while delta > epsi :
		nbiter += 1		
		x1 = g(x) # x1 joue le role de x_n+1
		delta = abs(x1 - x)
		x = x1
		print (x)
	return x, nbiter


def df(x) :
	return 2*x + 1

def h(x) :
	return x-((f(x))/(df(x)))

def newton(f, df, x0, epsi) :
	x = x0
	delta = 2*epsi
	nbiter = 0
	while delta > epsi :
		nbiter += 1		
		x1 = x-((f(x))/(df(x)))
		delta = abs(x1 - x)
		x = x1
		print (x)
	return x, nbiter

def dichotomie(f, a, b, epsi):	
	if b-a <= epsi : 
		return a,b
	else :
		c=(a+b)/2
	if f(a)*f(c)<=0:
		return dichotomie(f, a, c, epsi)
	else:
		return dichotomie(f, c, b, epsi)

"""	
def secante(f, x0, x1, epsi) :
	x = x0 # x joue le role de x_n
	delta = 2*epsi
	x2 = x1 # x2 joue le role de x_n-1	
	if delta > epsi :
		x3 = x - (((x-x2)/(f(x)-f(x2)))*f(x)) # x3 joue le role de x_n+1
		delta = abs(x3 - x)
		return x
	else :
		
		return secante(f, x3, x2, epsi)
"""

##############"   debut programme ###############"
import numpy as np
#import matplotlib.pyplot as plt



"""
# Exo 1
x = np.linspace(-1., 2., 100);
plt.plot(x, f(x))
plt.grid()
plt.show()


# Exo 2
x = np.linspace(-1., 2., 10);
plt.plot(x, g(x))
plt.grid()
plt.show()
"""

X=[]
x=1.0
k=1
while k < 26:
    x=g(x)
    X.append(x)
    k=k+1
    print(x)


print "\n"

#Point fixe :

#Test 1
x0= 1.0
epsi= 10**-15
r, nbiter = point_fixe(g, x0, epsi)
print r
print g(r)
print nbiter
print "\n"

#Test 2	
x0=-0.6
epsi= 10**-15
r, nbiter = point_fixe(g, x0, epsi)
print r
print g(r)
print nbiter
print "\n"


#Newton :

#Test 1
x0= 1.0
epsi= 10**-15
r, nbiter = newton(f, df, x0, epsi)
print r
print h(r)
print nbiter
print "\n"
	
#Test 2
x0=-1.0
epsi= 10**-15
r, nbiter = newton(f, df, x0, epsi)
print r
print h(r)
print nbiter
print "\n"


"""	
x0= 1.5
x1=2.0
epsi= 10**-12
r = secante(f, x0, x1, epsi)
print r
print f(r)
print "\n"

x0= -1.0
x1=0.0
epsi= 10**-12
r = secante(f, x0, x1, epsi)
print r
print f(r)
print "\n"
	
"""
# Dichotomie :

#Test1
a=1.5
b=2.0
epsi=1e-3
r = dichotomie(f, a, b, epsi)
print(r)

#Test2
a=-1.0
b=0.0
epsi=1e-3
r = dichotomie(f, a, b, epsi)
print(r)
