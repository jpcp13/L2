#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
from exo1 import f

def point_milieu(f,a,b,n) : 
    h = ( b - a ) / n
    S = 0
    for i in range (n):
        c = a + (h/2) * (2*i + 1)
        s = h * f(c)
        S+= s
    return S

#        x0 = a
#        xx = [x0]
#        for i in range (n+1):
#                x1 = x0 + ((b-a)/n)
#                xx.append(x1)
#                x0 = x1
        


#        cc = [] #creation d'une nouvelle liste vide
#        for i in range (n+1):
#                c = (xx[i] + xx[i+1])/2
 #               cc.append(c)
#		t0=clock()

#        ss = []
#        for i in range(n) :
#                s = ((b-a)/n)*f(cc[i+1])
#                ss.append(s)
#        t1=clock()
#        S = 0
#        for i in range(n) :
#                S += ss[i]
  
#	print('\n')
#	A = abs(S-I)
#	print('Erreur commise : ')
#	print(A)
#	print('\n')

#	t2 = t1 - t0
#	print('Le temps de calcul de l integrale est :')
#	print(t2)
#	print('\n')

#        return S

def p(x,n):
	if n>0:
		return x*p(x,n-1)
	else:
		return 1

#EXERCICE 2

#2A.

#Rendu papier

#2B.
"""
x0 = -0.5
xx = [x0]
for i in range (5):
        x1 = x0 + 0.25
        xx.append(x1)
        x0 = x1
        
print(x0)
print(xx)
print('\n')


cc = [] #creation d'une nouvelle liste vide
for i in range (5):
        c = (xx[i] + xx[i+1])/2
        cc.append(c)
        

t0 = clock ()

print('\n')

#2C.

ss = []
for i in range(4) :
        s = 0.25*f(cc[i+1])
        ss.append(s)
#print(ss)   
#print('\n')

t1 = clock ()

S = ss[0] + ss[1]  + ss[2] + ss[3]  
print('Somme de la surface') 
print(S) 
I = (sqrt(3)/4) + (pi/6)
print('\n')

A = abs(S-I)
print('Erreur commise : ')
print(A)
print('\n')

#2D.

t2 = t1 - t0
print('Le temps de calcul de l integrale est :')
print(t2)
print('\n')

#2F.
print('Test 1') 
a = -0.5
b = 0.5
n = 10
r = point_milieu(f, a, b, n)
print('Methode du point milieu')
print(r)
print('\n')
"""
#2G.
I = sqrt(3.0)/4 + (pi/6)

n = "n"
d = "erreur"
t = "temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))

print('-------------------------------------------------')

for i in range(6):
    t0 = clock()
    S = point_milieu(f, -0.5, 0.5, 10**(i+1))
    t1 = clock()
    r=abs(S-I)
    t2 = t1 - t0
    print('{0:10} | {1:13} | {2:10}'.format(10**(i+1),r,t2))


