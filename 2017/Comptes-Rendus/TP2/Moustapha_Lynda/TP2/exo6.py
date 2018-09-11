#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:04:23 2017

@author: 11608524
"""
import numpy as np
import matplotlib.pyplot as plt
from methodes import *
import time

#exo 6
#a

t= np.linspace(-np.pi, np.pi, 100)

x= np.cos(t)
y= np.sin(t)

plt.plot(x,y)
plt.grid('on')
plt.axis('equal')


#b
for i in range(10):
    xpoint = 2*np.random.rand()-1
    ypoint = 2*np.random.rand()-1
    if(xpoint**2+ypoint**2)<1:
        plt.scatter(xpoint,ypoint, color='blue' , marker='.')
    else:
        plt.scatter(xpoint,ypoint, color='pink', marker='.')
plt.savefig('Cercle monte_carlo')

#c
for i in range(1000):
    xpoint= 2*np.random.rand()-1
    ypoint=2*np.random.rand()-1
    if (xpoint**2+ypoint**2)<1:
        plt.scatter(xpoint,ypoint, color='red', marker='.')
    else:
        plt.scatter(xpoint, ypoint, color='green',marker='.')
plt.savefig('Cercle monte_carlo:')

print('Tableau avec la methode monte_carlo:')
print('        n |           erreur      |    temps (sec.)')
print('-----------------------------------------')
for i in range(1, 8):
    N=10**i
    start= time.clock()
    S=monte_carlo(1000)
    stop=time.clock()
    J= abs(S- np.pi)
    tps= stop-start
    print('{0:10g}| {1:20g}  | {2:10g}'.format(N, J, tps))
    i=i + 1

entete1= 'Tableau avec la methode monte_carlo:'
entete2='N     |erreur       | temps (sec.)'
with open ('Tableau4','w') as fichier:
    fichier.write(entete1+'\n')
    fichier.write(entete2+'\n')
    fichier.write

            
    
            