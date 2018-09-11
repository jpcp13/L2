import numpy as np
import matplotlib.pyplot as plt
from math import *
from moduletp3 import *


u0= 1.0
T=10.0
n=80
#a

def f(t, u):
	return -u
#b

tt,uu=euler(f, u0, T, n)

#c

def f1(t,u):
	return -u + t

def f2(t, u):
	return u**2

def f3(t, u):
	return u**2 - t 
