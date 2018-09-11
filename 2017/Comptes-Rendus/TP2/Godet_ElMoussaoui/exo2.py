from methods import point_milieu
from methods import enregistrer

def f(x) :
	import numpy as np	
	return np.sqrt(1 -x*x)



# Execution

S=0
x1=-0.5
x2=-0.25
import time as time
start = time.clock()

for i in range(4):
    
    ck=(x1+x2)/2
    s=0.25*f(ck)
    S = S + s
    x1=x1+0.25 
    x2=x2+0.25

elapsed = (time.clock() - start)
print "Integrale S:",S,"\nTemps de calcul de l'integrale:",elapsed,"\n"

#Tests
print "Test methode du point milieu \n"
n = 10
for i in range(6):
	print "Test entre -0.5 et 0.5 pour n =",n
	d,t = point_milieu(f,-0.5,0.5,n)
	d = d - - 0.52359877559
	print "Erreur:",d,"\n","Temps:",t,"\n"
	n = n * 10


enregistrer(point_milieu,f,'point_milieu',-0.5,0.5,6)
