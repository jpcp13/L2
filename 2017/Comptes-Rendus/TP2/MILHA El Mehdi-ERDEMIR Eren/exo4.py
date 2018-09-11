import matplotlib.pyplot as plt
#matplotlib.pyplot

from math import *

def f(x):
	import numpy as np
	return np.sqrt(1-x**2)


def Simpson(f,a,b,n) :
	h=(b-a)/float(n)
	z=(f(a)+f(b))/6
	for i in range(1,n) :
		z=z+f(a+i*h)/3
	for i in range(n) :
		z=z+f(a+(2*i+1)*h/2)*2/3
	return h*z

a =-0.5
b=0.5
n=10000
m = Simpson(f,a,b,n)
print m

#test n=10: 0.956611265864

#test n=100: 0.956611477469

#test n=1000: 0.956611477491

#test n=10000: 0.956611477491

#test n=100000: 0.956611477491


