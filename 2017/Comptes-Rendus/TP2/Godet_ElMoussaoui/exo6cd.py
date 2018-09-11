import numpy as np
import matplotlib.pyplot as plt
import math
import os
import time as time

I = 0
E = 0
N = 1000
for i in range(N):
	X = 2*np.random.rand()-1
	Y = 2*np.random.rand()-1
        if X > 1:
		X = cos(X)
	if Y > 1:
		Y = cos(Y)

	if ( X*X + Y*Y )< 1:
		plt.scatter(X,Y,color='r', marker = '.')
		I = I + 1

	else:
		plt.scatter(X,Y,color='green', marker = '.')
		E = E + 1

print "Exterieur:",E,"\nInterieur:",I
start = time.time()
Er = abs(4*I/N - math.pi )
r = time.time() - start
print "\nErreur :",Er
print " Temps :", r  

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
os.remove("cercle(annexe2).png")
plt.savefig('cercle(annexe2).png')

