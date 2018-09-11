#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:41:54 2017

@author: 11608524
"""

import math
import time
from methodes import *

#Exercice 2
#b)
def f(x):
        return math. sqrt(1-x**2)

'''
Création d'une liste
'''

depart = time.clock()
X=[]
C=[]
A=[]

#Création des valaurs de la liste (x0, x1,....,x5), append permet
#de regrouper tous les x


for i in range(5):
        x=-0.5 + 0.25*i
        X.append(x)
        
#On determine le milieu de chaque subdivision


for i in range(4):
    
        c=(X[i]+X[i+1])/2
        C.append(c)
        
#Calcul des aires f(c[i]) represente la hauteur


for i in range(4):
        
        a=(f(C[i])*(0.25))
        A.append(a)
        
#Calcul de l'aire totale sous la courbe en faisant la somme des 
#aires des petits rectangles


s=0
for i in range(4):
        s=A[i]+s
        
        
arrivee=time.clock()

temps_ecoule= arrivee -depart

print(temps_ecoule)

#f) Test de la fonction point milieu
    
# I represente l'integrale de la fonction

I=0.956611477

d = -0.5
b =0.5
n=1000
R = s - I

S=point_milieu(f ,d, b, n)

#g) Creation de tableau

for i in range(1,7):
    integral, temps = point_milieu(f, d, b, 10**i)
    err=abs(integral - I)
    print('{0:10d} | {1:e} |{2:.9e}'.format(10**i, err, temps))


#Creer le tableau dans un fichier externe


with open('fichier.txt','w') as fichier: #'w' pour ouvrir le fichier et lediter 
    for i in range(1,7):
        integral, temps= point_milieu(f,d,b, 10**i)
        err=abs(integral-I)
        fichier.write('{0:10d}| {1:e} | {2:.9e}\n'.format(10**i,
        err, temps))