from math import *
from time import *
from string import *
from pylab import *
from random import *
from fonctions import *

##### Affichage d'un tableau #####

with open('table3.txt', 'w') as tab:
	Z = '\t\tTableau correspondant a la fonction trapeze\n\n'
	tableau = Z+'N\t|\tErreur\t\t|\tTemps (sec.)\t\n'+ 68*'_'+'\n'
	print tableau
	tab.write(tableau)
	#print ('____________________________________________________________________\n')
	for i in range (1,7):
		x = p(10,i)
		t1 = clock()
		w = trapeze(f,-0.5,0.5,x)
		t2 = clock() - t1
		y = erreur(w)
		#espace = '\t' + '|' + '\t'
		s = repr(x) + '\t' + '|' + '\t' + '%.9f' % y + '\t|' + '\t' + '%.9f' % t2 + '\n'
		#ligne = "{0:7d} \t | \t {1:g} \t | \t {2:g}".format(x, y, t2)
		print(s)
		tab.write(s)
