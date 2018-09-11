import numpy as np 
from math import *
from time import *
from tp4 import *

x, dx = 2 , 1
X, Y, Points = [], [], [] 
while x <= 1000:
    y = p(x)
    
    point = (x, y) 
    
    X.append(x) 
    Y.append(y) 
    Points.append(point)
    x += dx


import matplotlib.pyplot as plt 
plt.clf()
plt.plot(X, Y, 'r')
plt.grid()
#plt.show()
plt.savefig('fig.png')

a, da = 2 , 1
A, B, P = [], [], [] 
while a <= 1000:
    
    b=a/log(a)
    P = (a, b) 
    
    A.append(a) 
    B.append(b) 
    Points.append(P)
    a += da



import matplotlib.pyplot as plt 
plt.clf()
plt.plot(X, Y, 'r')
plt.plot(A, B, 'c')
plt.grid()
#plt.show()
plt.savefig('fig.png')


