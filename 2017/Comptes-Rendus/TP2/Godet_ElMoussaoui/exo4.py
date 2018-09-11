from methods import simpson
from methods import enregistrer

def f(x) :
	import numpy as np	
	return np.sqrt(1 -x*x)


# Tests
print "Test methode de simpson \n"
n = 10
for i in range(6):
	print "Test entre -0.5 et 0.5 pour n =",n
	d,t = simpson(f,-0.5,0.5,n)
	d = d - 0.52359877559
	print "Erreur:",d,"\n","Temps:",t,"\n"
	n = n * 10

# Tableau
enregistrer(simpson,f,'simpson',-0.5,0.5,6)



