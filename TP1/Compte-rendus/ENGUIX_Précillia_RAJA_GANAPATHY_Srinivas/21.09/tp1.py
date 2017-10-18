#ENGUIX Precillia
#RAJA GANAPATHY Srinivas


#FONCTIONS

def f(x):
    return x**2 - x - 1
    
  
  
def g(x):
        return 1+(1/x)
    
        

def point_fixe(g,x0,epsi):
        x=x0
        d=2*epsi
        while d>epsi : 
                x1=g(x)
                d=abs(x1-x)
                x=x1
                print (x)
        return x          
  
  
  
def df(x):
        return 2*x-1.0       
        
  
        
def newton(f,df,x0,epsi):
        d=2*epsi
        x=x0
        cpt=0
        while d>epsi and cpt<40:
                cpt += 1
                v=x-f(x)/df(x)
                x=v
                print('x vaut {0} et cpt vaut {1}').format(x,cpt)
        return v



def dichotomie(f,a,b,epsi):
        if b-a<=epsi:
                print(a,b)
                return a,b
        else:
                c=(a+b)/2
                if f(a)*f(c)<=0:
                        return dichotomie(f,a,c,epsi)
                else:
                        return dichotomie(f,c,b,epsi)



def secante(f,x0,x1,epsi):
        delta= 2*epsi
        cpt=0
        while delta > epsi and cpt < 100:
                cpt +=1
                num = x1-x0
                delta= abs(num)
                den = f(x1)-f(x0)
                x2 = x1-num/den*f(x1)
                x0 = x1
                x1=x2
                print('x1 vaut {0} et x2 vaut {1} cpt vaut {2}').format(x1,x2,cpt)
        return x2                                          
   
                                         

#EXERCICE 1


x, dx = -1.0, 0.25
X, Y, Points = [], [], []


while x < 2:
        y = f(x)
        point = (x, y)

        X.append(x) 
        Y.append(y) 
        Points.append(point) 
        x += dx
print(X)
print(Y)
print('\n')

#Afficher un graphique 

import matplotlib.pyplot as plt
plt.plot(X, Y, '*r')
plt.grid()
plt.show()                
#plt.savefig('fig1.png')



#Exercice 2

#2a.

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()
#plt.savefig('fig2.png')


#2b.

x0=1.0
xn=[x0]
for i in range (25):
        x1 = g(x0)
        xn.append(x1)
        x0=x1
        
print(x0)
print(xn)
print('\n')


#EXERCICE 3

#3b.

#Test 1

a="Test 1 Point fixe"
print (a)

x0=1.0
epsi=10**-12

r=point_fixe(g,x0,epsi)
print('\n')

#Test 2

a="Test 2 Point fixe"
print (a)

y0=-0.6
epsi=10**-12

r=point_fixe(g,y0,epsi)
print('\n')


#EXERCICE4

#4a.

a='Verification des points fixe de f'
print(a)

x0=1.0
r=point_fixe(g,x0,epsi)

x0=-0.6
r=point_fixe(g,x0,epsi)
print('\n')

#4c.

#Test 1

a="Test 1 newton"
print(a)

x0=1.0
epsi = 1e-12
r=newton(f,df,x0,epsi)
print('\n')

#Test 2

a="Test 2 newton"
print(a)

x0=-1.0
epsi = 1e-12
r=newton(f,df,x0,epsi)
print('\n')


#EXERCICE 5

#Test 1

a="Test 1 secante"
print(a)     

x0=1.5
x1=2.0
epsi=1e-12
secante(f,x0,x1,epsi)
print('\n')

#Test 2

a="Test 2 secante"
print(a)     

x0=-1.0
x1=-0.5
epsi=1e-12
secante(f,x0,x1,epsi)
print('\n')


#EXERCICE 6

#Test 1

a="Test 1 Dichotomie"
print (a)

a=1.5
b=2.0
epsi=10**-12
dichotomie(f,a,b,epsi)
print('\n')

#Test 2

a="Test 2 Dichotomie"
print (a)

a=-1.0
b=0.0
epsi=10**-12
dichotomie(f,a,b,epsi)
print('\n')




