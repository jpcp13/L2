from methods import trapeze
from methods import enregistrer

def f(x) :
	import numpy as np	
	return np.sqrt(1 -x*x)


# Tests
print "Test methode du trapeze \n"
n = 10
for i in range(6):
	print "Test entre -0.5 et 0.5 pour n =",n
	d,t = trapeze(f,-0.5,0.5,n)
	d = d - 0.52359877559
	print "Erreur:",d,"\n","Temps:",t,"\n"
	n = n * 10

# Tableau
enregistrer(trapeze,f,'trapeze',-0.5,0.5,6)



