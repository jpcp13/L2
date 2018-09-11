#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:42:19 2017

@author: 11608524
"""
from methodes import *
import math


def f(x):
        return math. sqrt(1-x**2)


#Test de la fonction trapeze
    

a = -0.5
b =0.5
n=1000

#  5) Affichage des trois résuktats pour faire la comparaison

print(point_simpson(f,a,b,n))

print(trapeze(f,a,b,n))
print(point_milieu(f ,d, b, n))
