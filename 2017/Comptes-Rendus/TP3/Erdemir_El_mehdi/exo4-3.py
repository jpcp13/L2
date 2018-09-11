from math import *
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
from methods import euler


def u(t,u):
    return exp(-t)

X,Y = [],[]
X,Y = euler(u,1,2,10)

print X,Y





