#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:43:43 2017

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

print(trapeze(f,a,b,n))