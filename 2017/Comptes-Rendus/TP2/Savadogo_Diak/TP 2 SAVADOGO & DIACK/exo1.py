def f(x):
	from math import sqrt
	return sqrt(1-x**2)
	
import matplotlib.pyplot as plt
import time

x, dx = -0.5, 0.1
X, Y, Points = [], [], [] 
while x <= 0.5:
    y = f(x)
    point = (x, y) 
    
    X.append(x) 
    Y.append(y) 
    Points.append(point)
    x += dx

 

plt.plot(X, Y, 'y')
plt.grid()
#plt.show()
plt.savefig('figure2.png')



