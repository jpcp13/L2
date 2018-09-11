from math import *
from time import *
from string import *
from pylab import *
from random import *

def somme(A,B,dA,dB) : 
	C = []
	d = dA
	s = 0
	
	for i in range (0,d+1) : 
		
		s =  A[i]+B[i]
		C.append(s)

	return C


A = [1,1,1,1,1] # il faut changer les valeurs des degres a chaque fois 
print(C)
B = [1,1,1,1,0]
C = somme(A,B,4,4)
print(C)			
