#11502702 SABABADY Kamala 
#11502168 SELVARAJAH Dinusan 

#******************************************************
import time

#Partie 1 

def f(x):
	from math import sqrt
	return sqrt(1-x**2)

x, dx = -0.5, 0.01
X, Y, Points = [], [], [] 

while x < 0.5:
   	y = f(x)
    	point = (x, y) 
    	X.append(x) 
    	Y.append(y)
    	Points.append(point) 
    	x += dx


for point in Points:
   
    x = point[0] 
    y = point[1]
    if x >= 0.0: 
        print('{0:20.4f} {1:20.4f}'.format(x, y)) 



import matplotlib.pyplot as plt 
plt.plot(X, Y, 'r')
plt.grid()
plt.savefig('1.png')


#*********************************************************
