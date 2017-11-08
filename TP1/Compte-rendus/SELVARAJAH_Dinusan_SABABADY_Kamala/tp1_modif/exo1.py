#11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#******************************************************
import matplotlib.pyplot as plt 


#Partie 1 : x^2-x-1

#1.a)

def f(x):
    
   return x**2 - x - 1

x, dx = -1.0, 0.25
X, Y, Points = [], [], [] 

while x < 2:
   	y = f(x)
    	point = (x, y) 
    	X.append(x) 
    	Y.append(y)
    	Points.append(point) 
    	x += dx

print(X)
print(Y)
print("\n")

for point in Points:
   
    x = point[0] 
    y = point[1]
    if x >= 0.0: 
        print('{0:20.4f} {1:20.4f}'.format(x, y)) 
  
#1.b)    

print("\n")

import matplotlib.pyplot as plt 

plt.plot(X, Y, 'r')
plt.grid()
plt.savefig('1.png')



#1.c) Voir compte rendu 

#******************************************************
