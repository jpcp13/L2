#TP1

#Definition des fonctions

def  f(x) : 
	return x**2 -x -1
def df(x):

	return 2*x-1.0
	
def g(x) : 
    return 1+ 1.0/x 
    
# Exercice 1

#a)
x, dx = -1.0, 0.25
X, Y, Points = [], [], [] 

while x < 2 :
     y = f(x)
     point = (x, y) 
   
     X.append(x) 
     Y.append(y) 
     Points.append(point)
     x += dx
     
print(X)
print(Y)

for point in Points:
    
    x = point[0] 
    y = point[1]
    if x >= 0.0: 
    	print('{0:10.4f} {1:10.4f}'.format(x, y)) 
 
#b)
import matplotlib.pyplot as plt
plt.plot(X, Y,'r') 
plt.grid()
plt.show()
#c)Voir compte rendu

# Exercice 2

#a
# Representation sur l'intervalle positif 
import numpy as np
t = np.arange(1.0, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()

# Representation sur l'intervalle negatif 
t = np.arange(-2.0, -0.5, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b') 
plt.grid('on')
plt.axis('equal')
plt.show()

#b)
y=" Suite xn\n"
print(y)

x0=1.0
xx=[x0] #Enregistre les valeurs dans une liste
for i in range(25) :
	x1=g(x0)
	xx.append(x1)
	x0=x1
  
print(x0)
  
print(xx)

#c)Voir compte rendu	

# Exercice 3

#a)
def point_fixe(g, x0, epsi):
 #x1 joue le role de xn+1
 #x joue le role de xn
	x=x0 
	d=2*epsi
	cpt=0
	while d>epsi :
		cpt+=1
		x1=g(x) 
		d=abs(x1-x)
		x=x1
		print('x vaut : {0} et compteur vaut {1}\n'.format(x, cpt))
	return x
		
#b)
z=" Test de point fixe\n"
print(z)

 #Test1
x0=1.0
epsi=10**-12

r=point_fixe(g,x0,epsi)

 #Test2
x0=-0.6
epsi=10**-12

r=point_fixe(g,x0,epsi)

#c)Voir compte rendu

# Exercice 4

#a)
a='Verification que les points fixe  de g sont les zero de f\n'
print(a)

x0=1.0
r=point_fixe(g,x0,epsi)

x0=-0.6
r=point_fixe(g,x0,epsi)

#b)

def newton(f,df,x0,epsi):
	d = 2*epsi
	x = x0
	cpt = 0
	while d > epsi and cpt < 40 :
		cpt += 1
		x1=x-f(x)/df(x)
		d = abs(x-x1)
		x = x1
		print('x vaut : {0} et compteur vaut {1}\n'.format(x, cpt))
	return x1
	
#c)

#Test1
s="Test 1 newton\n"
print(s)

x0=1.0
epsi=1e-12
r = newton(f,df,x0,epsi)

#Test2
s="Test de newton\n"
print(s)

x0=-1.0
epsi=1e-12
r = newton(f,df,x0,epsi)

#Exercice 5

#a)
r="Test de Secante \n"
print(r)

def secante(f, x0, x1, epsi):
    #x0 va jouer le role de xn-1
    #x1 celui de xn
    d = 2*epsi
    cpt = 0
    while d > epsi and cpt < 40 :
        cpt += 1
        num = x1-x0
        d = abs(num)
        den = f(x1)-f(x0)
        x2 = x1-num/den*f(x1)
        x0 = x1
        x1 = x2
        print('x vaut : {0} et compteur vaut {1}\n'.format(x2, cpt))
    return x2
    
#b)
#Test 1
x0 = 1.5
x1 = 2.0
epsi=10**-12
r = secante(f,x0,x1,epsi)

#Test 2
x0 = -1.0
x1 = -0.5
epsi=10**-12
r = secante(f,x0,x1,epsi)

#Exercice 6

#a)
def dichotomie(f, a, b, epsi): 
	if b-a <= epsi:
		return a,b
	else:
		c=(a+b)/2
	if f(a)*f(c)<=0:
		return dichotomie(f,a,c,epsi)
	else:
		return dichotomie(f,c,b,epsi)	

#b)
p="Test de la dichotomie \n"
print(p)

#Test1
a = 1.5
b = 2.0
epsi=1e-12
r = dichotomie(f,a,b,epsi)
print(r)

#Test2
a = -1.0
b = 0.0
epsi=1e-12
r = dichotomie(f,a,b,epsi)
print(r)


	
	
	

