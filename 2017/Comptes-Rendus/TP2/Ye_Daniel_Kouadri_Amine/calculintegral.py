import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import time
from methode import *

I = 0.95661147749# valeur approximative de l'intregrale calculee

def f(x):
	return math.sqrt(1 - x**2)

x=np.linspace(-0.5,0.5,30)
y = [f(i) for i in x]
plt.grid()
plt.plot(x, y)
plt.savefig('f.png')

# enregistrer dans le fichier tableau_"string".txt, selon la methode, l'erreur et le temps dans un tableau pour le calcul de l'integrale de func de borne [a,b] et de precision allant de 10 jusqu'a 10^n
def enregistrer(methode, func, string, a, b, n):
	with open('tableau_{:s}.txt'.format(string), 'w') as fichier:
		print('{0:12s} | {1:9s} | {2:s}'.format('    erreur', ' temps (sec)', 'n'))
		fichier.write('{0:15s} | {1:12s} | {2:s}\n'.format('    erreur', ' temps (sec)', 'n'))
		for j in range(1, n+1):
			integral, temps = methode(func, a, b, 10**j)
			erreur = abs(integral - I)
			print('{0:e} | {1:e} | {2:d}'.format(erreur, temps, 10**j)) # envoi a l'ecran
			fichier.write('{0:.9e} | {1:e} | {2:d}\n'.format(erreur, temps, 10**j)) # envoie dans le fichier
		print('')

enregistrer(point_milieu, f, 'point_milieu', -0.5, 0.5, 6)
enregistrer(trapeze, f, 'trapeze', -0.5, 0.5, 6)
enregistrer(simpson, f, 'simpson', -0.5, 0.5, 6)
