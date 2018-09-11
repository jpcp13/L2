def f(x):
	return x**2 - x - 1

def df(x):
	return 2*x - 1

def g(x):
    return 1 + 1/x

def point_fixe(g, x0 ,epsi):
	x = x0 
	nbiter = 0
	delta = 2*epsi
	
	while delta > epsi :
		nbiter += 1
		x1=g(x) 
		delta = abs(x1-x)
		x=x1
		print (x)
	return x, nbiter

def newton(f, df, x0 ,epsi):
	nbiter = 0
	x = x0 
	delta = 2*epsi
	
	while delta > epsi :
		nbiter += 1
		x1 = x - f(x) / df(x)# c'est cici qu'on remplace g par x - f(x)/df(x)
		delta = abs(x1-x)
		x = x1
		print (x)
	return x, nbiter



	






###### Programme
#1-b) Graphique de f(x)
x, dx = -1.0, 0.1
X, Y, Points = [], [], [] 
while x <= 2:
    y = f(x)
    point = (x, y) 
    
    X.append(x) 
    Y.append(y) 
    Points.append(point)
    x += dx


import matplotlib.pyplot as plt 

plt.plot(X, Y, 'y')  ## Nous sauvegardons la figure 
plt.grid()
plt.show()
#plt.savefig('figure_1.png')


# Les 25 premiers termes de la suite
import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()

print("Les 25 premiers termes de la suite")
res=1.0
stock=[]
i=0
print(res)

for i in range (25):
	stock.append(res)
	res=(1+1/res)
	print(res)

print("\n")
#Methode du point fixe 
print("1er test point fixe:")
#test1 point fixe
x0 = 1.0
epsi = 1e-15
r, nbiter = point_fixe(g,x0,epsi)
print ('r = {0} et nbiter = {1}'.format(r, nbiter))
print ('g(r)={0}'.format(g(r)))

print("\n")
print("2eme test point fixe:")
#test2 point fixe
x0 = -0.6
epsi = 1e-15
r2, nbiter = point_fixe(g, x0, epsi)
print ('r2 = {0} et nbiter = {1}'.format(r2, nbiter))


print("\n")
#Methode de Newton
#test1 methode de newton
print('test1 methode de newton:')
x0 = 1.0
epsi = 1e-12
t, nbiter = newton(f, df, x0, epsi)
print ('t = {0} et nbiter = {1}'.format(t, nbiter))
print ('g(t)={0}'.format(g(t)))

print("\n")
#test2 methode de newton
print('test2 methode de newton:')
x0 = -1.0
epsi = 1e-12
t2, nbiter = newton(f, df, x0, epsi)
print ('t2 = {0} et nbiter = {1}'.format(t2, nbiter))
print ('g(t2)={0}'.format(g(t2)))



#Methode de la dichotomie

def dichotomie(f, a, b, epsi):
	nbiter = 0
	while b-a > epsi:
		nbiter += 1
		m = (a+b)/2
		if f(a)*f(m)> 0:
			a=m
		else: 
			b=m
	return m, nbiter


print("\n")
#test1 methode dichotomie
print("dichotomie test 1:")
a = 1.5
b = 2.0
epsi = 1e-12
t, nbiter = dichotomie(f, a, b, epsi)
print ('t1 = {0} et nbiter = {1}'.format(t, nbiter))

print("\n")
#test2 methode dichotomie
print("dichotomie test 2:")
a = -1.0
b = 0.0
epsi = 1e-12
t, nbiter = dichotomie(f, a, b, epsi)
print ('t2 = {0} nbiter = {1}'.format(t, nbiter))




## SAVADOGO Hamed
## DIACK Aliou






