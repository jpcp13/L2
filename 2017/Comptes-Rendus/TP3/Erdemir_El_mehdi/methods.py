from numpy import *
from matplotlib.pyplot import *
from math import sqrt
from numpy import *
import matplotlib.pyplot as plt
import time
from math import *
import numpy as np
from scipy.integrate import odeint
from time import clock



'''


def f(x):
    return x**2-x-1
x=linspace(-1.,2.,100)
plot(x,f(x))
show()




def f(x):
    return x**2-x-1



def g(x):
    return 1+(1/x)

x=linspace(-1.,2.,30)
plot(x,g(x))
show()

x=linspace(-1., 2., 30)
plot(x, f(x))
plot(x, g(x))
show()

X0=1.0
XX=[X0]
for i in range(25):
    X1=g(X0)
    XX.append(X1)
    X0=X1
    print(X0)
print(XX)

def g(x):
    return 1+(1/x)

def point_fixe(g,x0,epsi):
    x=x0 
    delta=2*epsi
    while delta>epsi:
        x1=g(x) 
        delta=abs(x1-x)
        x=x1
    return x 

x0=-0.6
epsi=1e-12
r= point_fixe(g,x0,epsi)
print r
print g(r)




def f(x):
    return x**2-x-1

def df(x):
    return 2*x-1

def g(x):
    return 1/1+x

def h(x):
    return x-f(x)/df(x)
'''
'''
def newton(f,df,x0,epsi):
    """" Entrees : f fonction , df sa derivee et x0 premiere estimation
                     prec precision(=epsilon)
         Sorties : x estimation de c une solution de f (x )=0 """
    x=x0
    delta=2*epsi
    while delta>epsi:
        x1=x-f(x)/df(x)
        delta=abs(x1-x)
        x=x1
        print x
    return x

x0=-1.0
epsi=1e-12
r=newton(h,x0,epsi)
print('r={0}'.format(r))
print('g(r)={0}'.format(g(r)))

print("\n")

print("\nTest Newton \n")
r1, nbiter2=point_fixe(f,1.0,1e-15)    
print "Nombre d'iteration :",nbiter2
print "r :  ",r1
print "f(r):",f(r)
'''

'''
def newton(f,df,x0,prec=0.0001):
    """" Entrees : f fonction , df sa derivee et x0 premiere estimation
                     prec precision(=epsilon)
         Sorties : x estimation de c une solution de f (x )=0 """
    y=f(x0)
    dy=df(x0)
    iprec=1/prec
    while abs(y)>prec and dy<iprec:
        x0=x0-y/dy
        y=f(x0)
        dy=df(x0)
    return x0


x0=1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print('r={0}'.format(r))
print('g(r)={0}'.format(g(r)))



def f(x):
    return x**2-x-1

def secante(f,x0,x1,epsi):
    delta=2*epsi
    while delta>epsi:
        num= x1-x0
        den=h(x1)-h(x0)
        x2=x1-(num/den)*f(x1)
        delta=abs(x2-x1)
        x0=x1
        x1=x2
    t=x1
    return t


x0=1.5
x1=2.0
epsi=1e-12


def f(x):
    return x**2-x-1

def dichotomie(f,a,b,epsi):
    err=abs(b-a)
    if f(a)*f(b)>0:
        return 'Il_faut_choisir_un_autre_intervalle'
    else:
        while err > epsi:
            c=0.5*(a+b);
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            err=0.5*err
        return c


a=-1.0
b=0.0
epsi=1e-12
t=dichotomie(f,a,b,epsi)
print t


def point_fixe(g,x0,epsi):
    x=x0 
    delta=2*epsi
    nbiter=0
    while delta>epsi:
        x1=g(x) 
        delta=abs(x1-x)
        x=x1
    r=x
    return r, nbiter





def newton(h,x0,epsi):
    delta=2*epsi
    nbiter2=0
    while delta>epsi:
        nbiter2 +=1
        x1=h(x0)
        delta=abs(x1-x0)
        x0=x1
    r=x0
    return r,nbiter2


def secante(f,x0,x1,epsi):
    delta=2*epsi
    nbiter3=0
    while delta>epsi:
        nbiter3+=1
        num= x1-x0
        den=h(x1)-h(x0)
        x2=x1-(num/den)*f(x1)
        delta=abs(x2-x1)
        x0=x1
        x1=x2
    t=x1
    return t, nbiter3

def dichotomie(f,a,b,epsi):
    g=a
    d=b
    nbiter4=0
    while (d-g)>2*epsi:
        nbiter4=nbiter4+1
        m= (d+g)/2
        if (f(g)*f(m))<= 0:
            d=m
        else:
            g=m
    return (d+g)/2, nbiter4




print("\nTest Point fixe \n")
r, nbiter1=point_fixe(g,1.0,1e-15)
print "Nombre d'iteration :",nbiter1
print "r :  ",r
print "g(r):",g(r)



print("\Test Secante \n")
r2, nbiter3=point_fixe(h,1.5,2,1e-15)
print "Nombre d'iteration :",nbiter3
print "r :  ",r2
print "h(r):",h(r)

print("\nTest dichotomie \n")
r3, nbiter4=point_fixe(f,1.5,2.0,1e-15)
print "Nombre d'iteration :",nbiter4
print "r :  ",r3
print "f(r):",f(r3)

print("\nTest Newton \n")
r1, nbiter2=point_fixe(f,1.0,1e-15)    
print "Nombre d'iteration :",nbiter2
print "r :  ",r1
print "f(r):",f(r)
'''

'''
def f(x):
	return np.sqrt(1-x**2)

#representation graphique sur [-0.5,0.5]
x = -0.5
dx = 0.1
X, Y, Points = [], [], []

while x < 0.5 :
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

#calcul de l'integrale I=0.95


def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a=-0.5
b=0.5


def point_milieu(f,a,b,n):
    s = 0
    s4 = 0.95
    temps = time.clock()
    for i in range(0,n):
        x1= a+(b-a)*i/float(n)
        x2= a+(b-a)*(i+1)/float(n)   
	s+=f((x1+x2)/2.0)*(x2-x1)
    return s, time.clock()-temps

for i in range(1,7):
    n = 10
    p_f = point_milieu(f, a, b, n**i)
    print('\n')
    print('{0}eme test point milieu = {1} '.format(i,p_f))




n1=10

n2=100
n3=1000
n4=10000
n5=100000
n6=1000000

print('\N')


I=0.95




def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a=-0.5
b=0.5

def trapezes(f,a,b,n) :
    h=float(b-a) / n
    s=0.0
    s += f(a)/2.0
    for i in range(1,n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h


print('_n')
for i in range (1,7):
    n=10
    t=trapezes(f , a, b, n**i)
    print('\n')
    print('{0}eme test trapezes = {1} ' .format(i,t))


def f(x):
	import numpy as np
	return np.sqrt(1-x**2)


def Simpson(f,a,b,n) :
	h=(b-a)/float(n)
	z=(f(a)+f(b))/6
	for i in range(1,n) :
		z=z+f(a+i*h)/3
	for i in range(n) :
		z=z+f(a+(2*i+1)*h/2)*2/3
	return h*z

a =-0.5
b=0.5
n=10000
m = Simpson(f,a,b,n)
print m

#test n=10: 0.956611265864

#test n=100: 0.956611477469

#test n=1000: 0.956611477491

#test n=10000: 0.956611477491

#test n=100000: 0.956611477491




#a.Cercle

theta = np.linspace(0,2*np.pi, 100)
Xcercle = np.cos(theta)
Ycercle = np.sin(theta)
plt.plot(Xcercle, Ycercle)
plt.axis("equal")
plt.show()
plt.savefig('cercle.png')

#b.
print('\n')
import numpy.random as npr
print('Quelques valeurs aleatoires entre -1 et 1:')
print(npr.uniform(-1,1,10))

#c.
for i in range(100):
    xpoint=2*np.random.rand()-1
    ypoint=2*np.random.rand()-1
    if (xpoint**2+ypoint**2)<1:
        plt.scatter(xpoint, ypoint, color='red',marker='.')
    else:
        plt.scatter(xpoint, ypoint, color='green',marker='.')

plt.xlim(-1.25, 1.25)
plt.savefig('cercle1.png')

plt.xlim(-1.25, 1.25)

def montecarlo(N):
    t=time.clock()
    cmpt=0
    for i in range(N):
        xpoint = 2*np.random.rand()-1
        ypoint =2*np.random.rand()-1
        if (xpoint**2+ypoint**2)<1:
            plt.scatter(xpoint, ypoint, color='red', marker='.')
            cmpt= cmpt +1
    S= (cmpt/float(N)*4)
    return S, time.clock()-t

#montecarlo
m_c, cmpt= montecarlo(10000)
print('2eme test montecarlo = {0} et le temps {1}'.format(m_c, cmpt))
'''

'''
def f(x):
	return np.sqrt(1-x**2)


x = -0.5
dx = 0.1
X, Y, Points = [], [], []

while x < 0.5 :
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


def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a=-0.5
b=0.5

def point_milieu(f,a,b,n):
    s = 0
    s4 = 0.95
    temps = time.clock()
    for i in range(0,n):
        x1= a+(b-a)*i/float(n)
        x2= a+(b-a)*(i+1)/float(n)   
	s+=f((x1+x2)/2.0)*(x2-x1)
    return s, time.clock()-temps

for i in range(1,7):
    n = 10
    p_f = point_milieu(f, a, b, n**i)
    print('\n')
    print('{0}eme test point milieu = {1} '.format(i,p_f))




n1=10

n2=100
n3=1000
n4=10000
n5=100000
n6=1000000

print('\N')


I=0.95

def enregistrer(methode, func, string, a, b, n):
    with open ('tableau {:s}.txt' .format(string), 'w') as fichier:
        print('{0:12s}| {2:s}\n' .format('Erreur', 'Temps(sec)', 'n'))
        fichier.write ('{0:15}|{1:12s}|{2:s}\n' .format( 'Erreur','Temps(sec)','n'))
        for j in range(1,n+1):
            integrale,Temps = methode(func,a,b,10**j)
            Erreur=abs(integrale - I)
            print('{0:e} | {2:d}' .format(Erreur, Temps, 10**j))
            fichier.write('{0:9e} | {1:e} | {2:d}\n' .format(Erreur, Temps, 10**j))
    print('')

p=enregistrer(point_milieu, f, 'point_milieu', -0.5, 0.5, 6)




p_f = point_milieu(f, a, b, n1)
print ('1er test = {0} '.format(p_f))
print('\n')

p_f = point_milieu(f, a, b, n2)
print ('2e test = {0} '.format(p_f))

print('\n')

p_f = point_milieu(f, a, b, n3)
print ('3e test = {0} '.format(p_f))


print('\n')

p_f = point_milieu(f, a, b, n4)
print ('4e test = {0} '.format(p_f))

print('\n')

p_f = point_milieu(f, a, b, n5)
print ('5e test = {0} '.format(p_f))



print('\n')

p_f = point_milieu(f, a, b, n6)
print ('6e test = {0} '.format(p_f))


import matplotlib.pyplot as plt


from math import *

def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a=-0.5
b=0.5

def trapezes(f,a,b,n) :
    h=float(b-a) / n
    s=0.0
    s += f(a)/2.0
    for i in range(1,n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h


print('_n')
for i in range (1,7):
    n=10
    t=trapezes(f , a, b, n**i)
    print('\n')
    print('{0}eme test trapezes = {1} ' .format(i,t))



def f(x):
	import numpy as np
	return np.sqrt(1-x**2)


def Simpson(f,a,b,n) :
	h=(b-a)/float(n)
	z=(f(a)+f(b))/6
	for i in range(1,n) :
		z=z+f(a+i*h)/3
	for i in range(n) :
		z=z+f(a+(2*i+1)*h/2)*2/3
	return h*z

a =-0.5
b=0.5
n=100000
m = Simpson(f,a,b,n)
print m





import matplotlib.pyplot as plt
import random
import math


x, y = [], []
for i in range(10000):
    a, b = random.uniform(-1.,1.), random.uniform(-1.,1.)
    x.append(a)
    y.append(b)
xyc = range( len( x ) )
plt.scatter(x,y,c = xyc, marker = '.', s=200)
plt.axis('equal')
plt.show()





x_inner, y_inner = [], []
x_outer, y_outer = [], []
for i in range(100000):
    a, b = random.uniform(-1.,1.), random.uniform(-1.,1.)
    length = math.sqrt(a**2 + b**2)
    if length < 1:
        x_inner.append(a)
        y_inner.append(b)
    else:
        x_outer.append(a)
        y_outer.append(b)
plt.scatter(x_inner, y_inner,c= 'red', marker = '.', s=200)
plt.scatter(x_outer, y_outer,c= 'blue', marker = '.', s=200)
print 4*len(x_inner)/float(len(x_inner) + len(x_outer)), math.pi
plt.axis('equal')
plt.savefig('W_direct_pi_color2.png')
plt.show()
'''


def f(x):
    return np.exp(-x)

x=0
dx=0.1
X,Y,Points=[],[],[]

while x<=2.1 :
    y=f(x)
    point=(x,y)
    X.append(x)
    Y.append(y)
    Points.append(point)
    x=x+dx
print(X)
print(Y)

plt.plot(X, Y, '*r')
plt.grid()
plt.show()




def u(t):
    return np.exp(-t)

def f(t , u):
    return -u


u0 = 1.0
T=2.0
n=10000
h=T/n
tt = np.linspace(0, T, n+1)
uu = np.zeros(n+1)
uu[0] = u0

for i in range(1, n+1):
    u1 = u0 - h*u0
    uu[i] = u1
    u0 = u1


plt.clf()
plt.grid()
plt.plot(tt, u(tt), '-r',tt,uu, '.k' )
plt.savefig('graphexo2.png')
plt.show()


plt.clf()
plt.grid()
plt.plot(tt, u(tt)-uu, '.r' )
plt.savefig('erreur_exo2.png')
plt.show()




def u(t):
    return np.exp(-t)

def f(t, u):
    return -u

def euler(f,u0,T,n):
    t0 = 0.0
    h = T/n
    tt = np.zeros(n+1)
    uu = np.zeros(n+1)
    uu[0] = u0
    tt[0] = t0
    for k in range(1,n+1):
        u1 = u0 + h*f(t0,u0)
        uu[k] = u1
        t1 = t0 + h
        tt[k] = t1
        u0 = u1
        t0 = t1
    return tt,uu




























