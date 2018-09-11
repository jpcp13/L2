from methode import *
def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

a =-0.5
b=0.5
n=1000000
l = trapezes(f,a,b,n)
print l
