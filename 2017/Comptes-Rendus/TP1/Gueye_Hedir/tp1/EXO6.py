#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#Partie 6: dichotomie
di="******Partie 6 : Dichotomie*******"
print(di)
print('\n')

# 6,a)
def dichotomie(f, a, b,epsi):
    compt = 0
    nbiter = 0
    if b-a<=epsi:
        compt +=1
        print(a,b)
        return a,b
        print('Le nombre diteration est ={0}').format(compt)

    else:
        compt +=1
        c=(a+b)/2
        if f(a)*f(c)<=0:
            return dichotomie(f,a,c,epsi)
            print('Le nombre diteration est ={0}').format(compt)
        else:
            return dichotomie(f,c,b,epsi)
            print('Le nombre diteration est ={0}').format(compt)

        
#6.b.i)
    
s="Test 1 Dichotomie"
print(s)
print("\n")

def f(x):

	return x**2-x -x-1

a=1.5
b=2.0
epsi=10**-12
r=dichotomie(f,a,b,epsi)
print('\n')