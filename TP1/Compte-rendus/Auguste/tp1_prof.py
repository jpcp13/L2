def f(x):
	return x**2-x - 1.0

def df(x):
	return 2*x - 1.0

def g(x):
	return 1+1/x
"""
def dg(x):
    return -1/(x**2)
"""

def dichotomie(f,a,b,epsi):
    g,d = a,b
    while (d-g) > 2*epsi :
        m = (d+g)/2
        if (f(g)*f(m)) <= 0 :
            d = m
        else :
            g = m
    return (d+g)/2


def point_fixe(g, X0, epsi):
    x = X0
    N = 2*epsi
    while N > epsi:
        x1 = g(X0)
        N = abs(x1-x)
        x = x1
    print (x)
    return x


def newton(f,df,x0,epsi):
    x = x0
    y = x0 - f(x0)/df(x0)
    while abs(y-x) >= epsi:
        x = y
        y = y - f(y)/df(y)
    return y

#########################" debut du programme; exos
import matplotlib.pyplot as plt

#Exo1


x = -1
dx = 0.1
X, Y, Points = [], [], []

while x < 2 :
	y = f(x)
	point =(x, y)
	X.append(x)
	Y.append(y)
	Points.append(point)
	x= x+dx
print(X)
print(Y)

plt.plot(X, Y, '*r')
plt.grid()
plt.show()

#Exo2
X0 = 1
XX = [X0]
for i in range(25):
	X1 = g(X0)
	XX.append(X1)
	X0=X1
	print(X0)
print(XX)

#Exo3
x0= -0.6
epsi = 1e-12 
r = point_fixe(g,x0,epsi)
print (r)
print (g(r))



# Exo 4
x0 =1.0 
epsi=1e-12
l = newton(f, df, 1.0, 1e-10)
print (l)
print (g(l))

#def secante(f,x0,x1,epsi):
#    x, y = x0, x1
#   while abs(y-x) > epsi :
#        x, y = y , (u*f(y)-y*f(x)/(f(y)-f(x))
#    return y


