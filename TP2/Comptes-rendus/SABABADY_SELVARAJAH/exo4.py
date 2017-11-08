# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#*********************************************************

from fonction import *

import time
def f(x):
	from math import sqrt
	return sqrt(1-x**2)

import math
from math import sqrt
I= math.pi/6 + sqrt(3)/4

 
n="n"
d="erreur"
t="temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))
t="---------------------------------------------"
print(t)

for i in range(1,7):
    t5=time.clock()
    p= Simpson(f,-0.5,0.5,10**(i))
    t6=time.clock()
    r=abs(p-I)
    y=t6-t5
    print('{0:10} | {1:13} | {2:10}'.format(10**(i),r,y))

print('\n')

titre = 'METHODE DE SIMPSON:'
entete = '{0:15s}|{1:15s}|{2:15s}'. format('n','erreur','temps')
tirets = '-'*42

with open('simpson.txt','w') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(entete+'\n')
    fichier.write(tirets+'\n')
    for i in range (1,7):
        t5=time.clock()
        p= Simpson(f,-0.5,0.5,10**(i))
        t6=time.clock()
        r=abs(p-I)
        y=t6-t5
        ligne = '{0:15d}|{1:15g}|{2:15g}'. format(10**(i), r, y)
        fichier.write(ligne+'\n')
    fichier.write('\n')
    

