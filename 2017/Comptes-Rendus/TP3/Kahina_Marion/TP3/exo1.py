from module import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

#Representation graphique de u

x, dx = 0, 0.1
X, Y, Point = [], [], [] 

while x < 2:
   	y = u(x)
    	pt = (x, y) 
    	X.append(x) 
    	Y.append(y)
    	Point.append(pt) 
    	x += dx

plt.plot(X, Y, 'g')
plt.grid()
plt.savefig('CourbeU.png')


