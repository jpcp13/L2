#2-a,b,c) Voir compte rendu
#2-e) Fonction Point_milieu (voir methods.py)
#2-f) Tests
a = -0.5
b = 0.5

n1 = 10
n2 = 100
n3 = 1000
n4 = 10000
n5 = 100000
n6 = 1000000

#METHODE DU POINT MILIEU SANS LA BOUCLE
"""
#1er test
p_f = point_milieu(f, a, b, n1)
print ('1er test = {0} '.format(p_f))

print('\n')
#2e test
p_f = point_milieu(f, a, b, n2)
print ('2e test = {0} '.format(p_f))

print('\n')
#3e test
p_f = point_milieu(f, a, b, n3)
print ('3e test = {0} '.format(p_f))

print('\n')
#4e test
p_f = point_milieu(f, a, b, n4)
print ('4e test = {0} '.format(p_f))

print('\n')
#5e test
p_f = point_milieu(f, a, b, n5)
print ('5e test = {0} '.format(p_f))

print('\n')
#6e test
p_f = point_milieu(f, a, b, n6)
print ('6e test = {0} '.format(p_f))
"""
from methods import *
import time


#2-g) METHODE POINT_MILIEU a l'aide d'une boucle
"""
for i in range (1, 7):
	n = 10
	p_f = point_milieu(f, a, b, n**i)
	print('\n')
	print('{0}eme test point milieu = {1} '.format(i,p_f))
"""
#Tableau

def enregistrer(methode, func, string, a, b, n):
	with open ('tableau {:s}.txt' .format(string), 'w') as fichier :
		print('{0:12s} |  {2:s}\n'.format(' Erreur', 'Temps(sec)', 'n'))
		fichier.write ('{0:15}|{1:12s}|{2:s}\n' .format( 'Erreur','Temps(sec)','n'))
		for j in range(1, n+1):
				integrale,Temps = methode(func,a,b,10**j)
				Erreur=abs(integrale - I)
				#~ print('{0:e} | {2:d}' .format(Erreur, Temps, 10**j))
				fichier.write('{0:9e} | {1:e} | {2:d}\n' .format(Erreur, Temps, 10**j))
	print('')

p = enregistrer(point_milieu, f, 'point_milieu', -0.5, 0.5, 6)





