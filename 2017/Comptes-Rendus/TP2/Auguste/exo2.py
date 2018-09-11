from methode import *

def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

n = point_milieu(f,-0.5 ,0.5,1000000)
print n

#p = enregistrer(point_milieu,f,'point_milieu',-0.5,0.5,6)
