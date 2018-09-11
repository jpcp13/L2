from math import *
from time import *
from string import *
from pylab import *
from random import *

def derivation(A): 
	
	for i in range(0,len(A)-1) :
		
		A[i]  = (i+1)*A[i+1]
		
		
	return A

A = [1,3,9,5,2]
C = derivation(A)
print(C)




















	
			
