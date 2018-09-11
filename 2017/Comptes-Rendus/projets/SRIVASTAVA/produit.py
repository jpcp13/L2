from math import *
from time import *
from string import *
from pylab import *
from random import *

def produit(A,B,dA,dB) : 
	C = []
	for k in range(dA+dB+1):
		s = 0
		for i in range(k+1) :
			if (i<=dA) and (k-i <= dB) : 
				s =  s + A[i]*B[k-i]

		C.append(s)
	return C

A = [1,2,1] 
B = [1,1]
C = produit(A,B,2,1) # il faut changer les valeurs des degres a chaque fois 
print(C)
