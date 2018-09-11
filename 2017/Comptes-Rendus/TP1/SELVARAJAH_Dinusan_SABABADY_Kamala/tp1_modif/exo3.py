# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 


from methods import *
#******************************************************
#Partie 3 : Point Fixe


def g(x):
	return 1+1/x





pt="*** Partie 3 : Point Fixe ***"
print(pt)
print('\n')

#3.a)
"""
migration de point_fixe vers module
"""

#3.b)


#Test 1
n= " Test 1 Point fixe"
print(n)
print("\n")
x0=1.0
epsi=10**-12

r= point_fixe(g,x0,epsi)
print("\n")

#Test 2
n=" Test 2 Point fixe"
print(n)
print("\n")
x0=-0.6
epsi=10**-12

r= point_fixe(g,x0,epsi)

print("\n")
#3.c)

#******************************************************
