import numpy as np 
from math import *
from time import * 
from tp4 import *

#premier test
S = p(10000)
print S

print('      n |  pi(n) | n/log(n) ')
print('---------------------------------')
for i in range(1,8):
	n = 10**i
	
	S = p(n)
	
	E = n/log(n)

	print(' {0}  | {1}   | {2}  '.format(n,S,E))


entete = '      n |  pi(n) | n/log(n) '
pointilles = '---------------------------------'


with open ("tableau.txt", "w") as fichier:
	fichier.write(entete + '\n')
	fichier.write(pointilles + '\n')
	for i in range(1,8):
		n = 10**i
		tps1 = clock()
		S = p(n)
		T = n/log(n)
		fichier.write(' {0}  | {1}   | {2}  \n'.format(n,S,T))

