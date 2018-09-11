from methods import *

erreur,temps = Monte_Carlo_boule(1000)
print erreur,"\n",temps

enregistrer_carlo(Monte_Carlo_boule, 'exo6g',6)
