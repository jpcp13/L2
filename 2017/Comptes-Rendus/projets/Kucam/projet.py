from operator import mul
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np


t = np.arange(-1.0, 1.0, 0.0001)

# Combinaison binomiale

def nCk(n,k):
	return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# Polynome de Tchebychev

def tchebychev(n, x):
	return np.sum([ (nCk(n, 2*k) * x ** (n - 2*k) * (x**2 - 1) ** k) for k in range(0,(n/2)+1) ])

# Fonction de dessin

def drawTchebychev(n):
	T = [tchebychev(n,i) for i in t]
	plt.plot(t,T, "-", color='black')
	plt.title(u'$T_n$ pour $n='+str(n)+'$', fontsize=20)
	plt.grid(True)
	plt.show()


drawTchebychev(1)
drawTchebychev(2)
drawTchebychev(3)
drawTchebychev(4)
drawTchebychev(5)
drawTchebychev(6)
drawTchebychev(7)

#Quelques fonctions utiles pour un polynome p donne.
#Coefficient de X**k pour un polynome p donne.

def coef(p,k):
  if k<len(p):
    return p[k]
  else:
    return 0

#Calcul du degre de p, on peut montrer que pour tout n, deg(Tn) = n
def deg(p):
    d=0
    for k in range(len(p)):
        if p[k]!=0: d=k
    return d
