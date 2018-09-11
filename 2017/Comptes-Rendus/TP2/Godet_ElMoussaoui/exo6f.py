from methods import *


def enregistrer_carlo(methode,string, n):
	with open ('tableau_{:s}.txt'.format(string),'w') as fichier :
        	print('{0:12s} | {1:9s} | {2:s}'.format('    erreur', ' temps (sec)', 'n'))
 	        fichier.write('{0:15s}|{1:12s}|{2:s}\n'.format('    erreur', ' temps (sec)', 'n'))
	        for j in range(1, n+1):
			erreur,temps = methode(10**j)
			print('{0:e} | {1:e} | {2:d}' .format(erreur, temps, 10**j))
			fichier.write('{0:9e} | {1:e} | {2:d}\n'. format(erreur, temps, 10**j))
	print('') 


enregistrer_carlo(Monte_Carlo,'carlo',6)
