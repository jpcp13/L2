#4) METHODE DE SIMPSON
from methods import *

for i in range (1, 7):
	n = 10
	simp= simpson(f, a, b, n**i)
	print('\n')
	print('{0}eme test simpson = {1} '.format(i,simp))

