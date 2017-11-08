# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#******************************************************

def f(x):
   return x**2 - x - 1

    
from methods import *

#Partie 6 : Dichotomie

di="****** Partie 6 : Dichotomie ******"
print(di)
print('\n')

# 6.a)
"""
migration de dichotomie vers module
"""
#6.b.i)

s="Test 1 Dichotomie"
print(s)
print("\n")

a=1.5
b=2.0
epsi=10**-3
r=dichotomie(f,a,b,epsi,0)
print('\n')

#6.b.ii)

t="Test 2 Dichotomie"
print(t)
print("\n")

a=-1.0
b=0.0
epsi=10**-3
r=dichotomie(f,a,b,epsi,0)
print('\n')


for i in range(5):
	a=1.5
	b=2.0
	epsi=10**-((i+1)*3)
	print((i+1)*3)
	r=dichotomie(f,a,b,epsi,0)
	print('\n')
#******************************************************
