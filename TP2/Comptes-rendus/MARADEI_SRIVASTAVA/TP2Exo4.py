from math import *
from time import *
from string import *
from pylab import *
from random import *
from fonctions import *

    
##### Affichage d'un tableau #####

with open('table4.txt', 'w') as tab:
	Z = '\t\tTableau correspondant a la fonction Simpson\n\n'
	tableau = Z+'N\t|\tErreur\t\t|\tTemps (sec.)\t\n'+ 68*'_'+'\n'
	print tableau
	tab.write(tableau)
	for i in range (1,7):
		x = p(10,i)
		t1 = clock()
		w = simpson(f,-0.5,0.5,x)
		t2 = clock() - t1
		y = erreur(w)
		s = repr(x) + '\t' + '|' + '\t' + '%.9f' % y + '\t|' + '\t' + '%.9f' % t2 + '\n'
		print s
		tab.write(s)

