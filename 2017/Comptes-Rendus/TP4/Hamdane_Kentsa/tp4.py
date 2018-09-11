import matplotlib.pyplot as plt
from fonctiontp4 import *

#exo 1
#e
for i in range(1, 6):
	if is_prime(Fn(i)):
		print('le nombre de fermat {0} est premier'.format(Fn(i)))
	else:
		print('le nombre de fermat {0} n est pas premier'.format(Fn(i)))
#exo 2
#c
P = primes(1000)
with open('primes','w') as fichier:
	fichier.write('Tableau contenant tous les entiers de 1 a 1000\n')
	fichier.write('-------------------------------------------------------\n')
	cpt = 0
	for p in P:
		cpt += 1
		fichier.write('{0}  '.format(p))
		if cpt%10 == 0:
			fichier.write('\n')
#d

with open('tableau','w') as fichier2 :
	fichier2.write('Tableau contenant pi(n) et n/log(n) en fonction de n\n')
	fichier2.write('-------------------------------------------------------\n')
	fichier2.write(' n         |      pi(n)     |    n/ln(n)     \n')
	for i in range(1, 7):
		n = 10**i
		ligne = '{0:g}|    {1:g}         |{2:g}         \n'.format(n ,pi(n) , f(n))
		fichier2.write(ligne)

plt.clf()
for i in range(2,100):
	plt.plot(i, pi(i) ,'+r',i,f(i),'+k')
plt.grid('on')
plt.axis('equal')
plt.savefig('Graphique')


