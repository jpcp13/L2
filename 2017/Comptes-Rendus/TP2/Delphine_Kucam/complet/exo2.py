
import numpy as np
import matplotlib.pyplot as plt
import time
import math
from integration import *

I = (math.pi/6)+(math.sqrt(3)/4) #calculer a la main

# exo2_b

x0=-0.5
x1=-0.25
x2=0
x3=0.25
x4=0.5


S1= f((x0+x1)/2)*0.25
S2= f((x2+x1)/2)*0.25
S3= f((x2+x3)/2)*0.25
S4= f((x3+x4)/2)*0.25
Sk= S1+S2+S3+S4
print('Sk=', Sk)

#exo2_c erreur commise
erreur_commise= abs(Sk-I)
print('erreur_commise=', erreur_commise)
n = 10**4
a = 0


#exo2_d


print('n\terreur\t\ttemps\t')
print('-----------------------------------------------')
for i in range (1,7):
	x = 10**i
	t1 = time.clock()
	S = point_milieu(f,-0.5,0.5,10**i)
	delta =time.clock() - t1
	erreur = abs(S-I)
	print('{0:>7d}  {1:>.3e}  {2:>.3e}'.format(x, erreur, delta))
	
with open('tabpointmilieu','w') as fichier:
	fichier.write('n\terreur\t\ttemps\t\n')
	fichier.write('-----------------------------------------------\n')
	for i in range (1,7):		
		x = 10**i
		t1 = time.clock()
		S = point_milieu(f,-0.5,0.5,10**i)
		delta =time.clock() - t1
		erreur = abs(S-I)
		ligne ='{0:>7d}  {1:>.3e}  {2:>.3e}'.format(x, erreur, delta)
		fichier.write(ligne + '\n')

