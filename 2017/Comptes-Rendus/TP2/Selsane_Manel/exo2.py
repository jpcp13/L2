from tp2 import *
from time import clock
from math import pi 


#Exercice 2

#a) voir papier

#b)

x0 = -0.5
xx = [x0] #Enregistre les poins x_i de la subdivision dans une liste
for i in range(5) :
        x1 = x0 + 0.25
        xx.append(x1)
        x0 = x1

print('xi:\n')  
print(xx)
print('\n')

cc = [] #Enregistre les milieux dans une liste
for i in range(5) :
        c = (xx[i] + xx[i+1])/2 
        cc.append(c)

print('ci:\n')
print(cc)
print('\n')

t0 = clock() #Temps avant le calcul de l'integrale

ss = []  
for i in range(4) :

        s = (0.25)*f(cc[i+1])
        ss.append(s)
print(ss)
print('\n')

S = ss[0]+ss[1]+ss[2]+ss[3]
print('S = ')
print(S)
print('\n')

t1 = clock() #Temps apres le calcul de l'integrale

#c) 

I = sqrt(3)/4+ pi/6 #Integrale calcule a la main
V = abs(S-I)
print('Erreur commise :\n')
print(V)
print('\n')

#d)
print('Temps de calcul:\n')
t2 = t1 - t0
print(t2)
print('\n')

#e) voir fichier tp2.py

#f)

print('Test point mileu:\n')

p = pt_milieu(f,-0.5,0.5,10) 
print(p)
print('\n')

V = abs(p-I)
print('Erreur avec point milieu :\n') 
print(V)
print('\n')

#g) 

n = "n"
d = "erreur"
t = "temps (sec.)"

print('{0:10}| {1:10}      | {2:10}'.format(n,d,t))

t = "----------------------------------------------"
print( t)

for i in range(1, 6):
	t6 = clock()
	p = pt_milieu(f,-0.5,0.5,10**i)
	t7 = clock()
	V = abs(p-I)
	t8 = t7-t6

	print('{0:10}|{1:10}|{2:10}'.format(10**i,V,t8))

