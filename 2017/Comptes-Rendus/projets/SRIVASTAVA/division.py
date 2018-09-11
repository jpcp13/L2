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



def somme(A,B,dA,dB) : 
	C = []
	d = dA
	s = 0
	
	for i in range (0,d+1) : 
		
		s =  A[i]+B[i] # il faut changer les valeurs des degres a chaque fois 

		C.append(s)

	return C


 
def monome(dR,a,b) : 
	C = R
	for i in range (dR+1):
		if (i == b) : 
			C[i]=a
		else :
			C[i] = 0
			
	 
			
	return C

def division(A,B) : 
	Q = [0]
	P = []
	R = A # c est le reste intermediaire 
	
	while ( len(R) >= len(B)) : 
		P = monome(len(R),R[len(R)],len(R)-len(B)) 
		R = somme(R,produit(-P,B))
		Q = somme(Q,R)
		dR = dR-1
	return Q,R

A = [-1,3,-2,-1,2]
B = [1,-1,1]

Q,R = division(A,B)
print(Q)
print(R)




















	
			
