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


#Partie 5 : Secante

#5.a)

se="***** Partie 5 : Secante *****"
print(se)
print('\n')


#5.b)

#Test 1
print("\n")
si=" Test 1 Secante"
print(si)
print("\n")

x0=1.5
x1=2.0
epsi=1e-2
secante(f,x0,x1,epsi)
print("\n")

#Test 2
print("\n")
sa=" Test 2 Secante"
print(sa)
print("\n")

x0=-1.0
x1=-0.5
secante(f,x0,x1,epsi)
print("\n")


#******************************************************
