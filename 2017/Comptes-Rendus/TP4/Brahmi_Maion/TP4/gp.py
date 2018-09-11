import numpy as np 
from math import *
from time import *
from tp4 import *

x, dx = 2 , 1
K, B, Points = [], [], [] 
while x <= 1000:
    y = p(x)
    
    point = (x, y) 
    
    K.append(x) 
    B.append(y) 
    Points.append(point)
    x += dx


"""import matplotlib.pyplot as plt 
plt.clf()
plt.plot(X, Y, '*m')
plt.grid()
#plt.show()
plt.savefig('graph1.png')"""

x, dx = 2 , 1
X, Y, Points = [], [], [] 
while x <= 1000:
    
    y=x/log(x)
    point = (x, y) 
    
    X.append(x) 
    Y.append(y) 
    Points.append(point)
    x += dx


import matplotlib.pyplot as plt 
plt.clf()
plt.plot(K,B,'m',X, Y, 'g')
plt.grid()
#plt.show()
plt.savefig('graph1.png')


