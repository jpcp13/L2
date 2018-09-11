import matplotlib.pyplot as plt
from numpy import *
from math import *
from pylab import *
from methods import euler


def u(t,u):
	return exp(-t)

X,Y = [],[]
X,Y = euler(u,1,2,10)

print X,Y
