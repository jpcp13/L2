from math import *
from time import *
from string import *
from pylab import *
from random import *
from fonctions import *

###### EXO 2 ######

t1 = clock()
A = point_milieu(f,-0.5,0.5,4) #S4 = A
t2 = clock() - t1
print A
print t2
ERREUR = erreur(A)
print ERREUR

##### Affichage du Tableau ####
with open('table2.txt', 'w') as tab:
	Z = '\t\tTableau correspondant a la fonction point milieu\n\n'
	tableau = Z+'N\t|\tErreur\t\t|\tTemps (sec.)\t\n'+ 68*'_'+'\n'
	tab.write(tableau)
	print tableau
	for i in range (1,7):
		x = p(10,i)
		t1 = clock()
		w = point_milieu(f,-0.5,0.5,x)
		t2 = clock() - t1
		y = erreur(w)
		s = repr(x) + '\t' + '|' + '\t' + '%.9f' % y + '\t|' + '\t' + '%.9f' % t2 + '\n'
		print s
		tab.write(s)



