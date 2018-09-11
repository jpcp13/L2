from tp2 import *
from math import pi
from time import clock

#f)
print('Test simpson :\n')

p = trapeze(f,-0.5,0.5,4) 
print(p)
print('\n')


#g)
I = sqrt(3)/4+ pi/6 #Integrale calcule a la main
n = "n"
d = "erreur"
t = "temps (sec.)"

print('{0:10}| {1:10}      | {2:10}'.format(n,d,t))

t = "----------------------------------------------"
print( t)

for i in range(1, 6):
	t6 = clock()
	p = simpson(f,-0.5,0.5,10**i)
	t7 = clock()
	V = abs(p-I)
	t8 = t7-t6

	print('{0:10}|{1:10}|{2:10}'.format(10**i,V,t8))

