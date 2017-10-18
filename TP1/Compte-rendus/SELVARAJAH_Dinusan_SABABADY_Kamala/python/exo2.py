# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#******************************************************
import matplotlib.pyplot as plt 

#Partie 2 : 1+1/x

#2.a)
def g(x):
	
	return 1+1/x

import numpy as np
t = np.arange(1.5, 2.0, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()


import numpy as np
t = np.arange(-2.0, -0.5, 0.01)
plt.plot(t, g(t), 'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()



#2.b)

x0=1.0
xn=[x0]
for i in range(25):
	x1=g(x0)
	xn.append(x1)
	x0=x1

print (x0)
print (xn)
print("\n")

#2.c) voir compte rendu

#******************************************************
