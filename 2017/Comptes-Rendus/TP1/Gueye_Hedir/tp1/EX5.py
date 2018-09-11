#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:10:55 2017

@author: 11608524
"""

def f(x):

	return x**2-x -1


#Partie 5: Secante

se="****Partie 5 : Secante****"
print(se)
print('\n')

def secante(f,x0, x1, epsi):
    delta=2*epsi
    compt=0
    nbiter=0
    while delta> epsi and compt<100:
        compt+=1
        num= x1-x0
        delta= abs(num)
        den= f(x1)-f(x0)
        x2=x1-((num/den)*f(x1))
        x0=x1
        x1=x2
        print('x={0},compteur ={1}\n'.format(x2,compt))
    print('Le nombre diteration est ={0}'.format(compt))
    return x2, nbiter
#5.b)


#Test 1

print("\n")
si=" Test 1 Secante"
print(si)
print("\n")


x0=1.5
x1=2.0
epsi=1e-12
r= secante(f,x0,x1,epsi)
print("\n")

#Test 2
print("\n")
sa="Test 2 Secante"
print(sa)
print("\n")

x0=-1.0
x1=-0.5
epsi=1e-12
r= secante(f,x0,x1,epsi)
print("\n")
    