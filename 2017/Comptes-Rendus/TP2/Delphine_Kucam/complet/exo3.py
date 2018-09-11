import numpy as np
import matplotlib.pyplot as plt
import time
import math
from integration import *

I=((math.pi)/6)+(math.sqrt(3)/4) #calculer a la main

print('      n     erreur       temps')
print('------------------------------')
for i in range (1, 6):
	x = 10**i
	t1 = time.clock()
	S = trapeze(f,-0.5,0.5,10**i)
	delta = time.clock() - t1
	erreur = abs(S-I)
	print('{0:>7d}  {1:>.3e}  {2:>.3e}'.format(x, erreur, delta))
"""
with open('tabtrapeze','w') as fichier:
	fichier.write('n\terreur\t\ttemps\t\n')
	fichier.write('-----------------------------------------------\n')
	for i in range (1,7):		
		x = 10**i
		t1 = time.clock()
		S = trapeze(f,-0.5,0.5,10**i)
		delta =time.clock() - t1
		erreur = abs(S-I)
		ligne ='{0:>7d}  {1:>.3e}  {2:>.3e}'.format(x, erreur, delta)
		fichier.write(ligne + '\n')
"""
