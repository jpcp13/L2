# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 




#******************************************************
def g(x):
	return 1+1/x

def f(x):
   return x**2 - x - 1
   
def df(x):
	return 2*x-1.0
    
    
    
    
from methods import *


#Partie 4 : Newton

ne="**** Partie 4 : Newton ****"
print(ne)
print('\n')

#4.a)

d="Verification de g"
print(d)



epsi=10**-12
x0=1.0
r= point_fixe(g,x0,epsi)
print('\n')
x0=-0.6
r= point_fixe(g,x0,epsi)

#4.b)
def df(x):
	return 2*x-1.0


#4.c)
"""
migration de newton vers module
"""
#Test 1
print("\n")
n=" Test 1 NEWTON"
print(n)
print("\n")

x0=1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print("\n")

#Test 2
n2=" Test 2 NEWTON"
print(n2)
print("\n")

x0=-1.0
epsi=1e-12
r=newton(f,df,x0,epsi)
print("\n")

#******************************************************
