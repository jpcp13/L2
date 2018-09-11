from fonctions import * 
from math import * 
from string import *
from pylab import *

def LOG(x):
	return x/log(x)

### EXERCICE 2 QUESTION C ###

with open('primes.txt', 'w') as p
	S = primes(1000)
	p.write(repr(S))

### EXERCICE 2 QUESTION D ### 

X = []
Y = [] 
N = 4000

for i in range(1,N):
	X.append(i)	
for i in range(1,N):
	Y.append(Pi(i))

clf()
plot(X,Y,'r')
x = linspace(1,N)
y = LOG(x)
plot(x,y,'b')
grid()
show()

with open('table.txt', 'w') as tab:
	Z = '\t\tTable \n\n'
	tableau = Z+'n\t|\tPi(n)\t\t|\tn/log(n)\t\n'+ 68*'_'+'\n'
	print(tableau)
	tab.write(tableau)
	for i in range (1,3):
		x = 10**i
		y = Pi(x)
		z = LOG(x)
		s = repr(x) + '\t' + '|' + '\t' + '%.9f' % y + '\t|' + '\t' + '%.9f' % z + '\n'
		print(s)
		tab.write(s)

# L affichage dans le fichier texte peut ne pas etre correcte. En revanche tout fonction bien dans le terminal. 



