#3) METHODE DES TRAPEZES
from methods import *

for i in range (1, 7):
	n = 10
	t= trapezes(f, a, b, n**i)
	print('\n')
	print('{0}eme test trapezes = {1} '.format(i,t))


print('\n')


