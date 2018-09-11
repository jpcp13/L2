import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import random


def is_prime(n):
        if n == 1 or n == 0:
                return False
        if n == 2:
                return True
        for i in range(2, int(np.sqrt(n))+2):
                if n%i==0:
                        return False
        return True
                
def primes(n):
        p = []
        for i in range(1, n+1):
                if is_prime(i):
                        p.append(i)
        return p

def rdm_prime(n1, n2):
        r=0
        while(not is_prime(r)):
                r=random.randint(n1,n2)

def cribe_era(n):
        l=[]
        for i in range(2,n+1):
             l.append(i) ## on remplit la liste avec tous les nombres de 2 a n pour eliminer ensuite les nombres qui ne sont pas premiers
        r=0
        while(l[r]<=int(np.sqrt(l[len(l)-1]))):## la boucle s'arrete quand le carrée du plus petit nombre restant dans la liste est supérieur au dernier nombre restant dans la liste 
                for j in range(2,(n//l[r])+1):
                        if (l[r]*j) in l: 
                                l.remove(l[r]*j) ## on elimine les nombres multiples des nombres restants dans la liste
                r=r+1 ##on passe au nombre suivant pour eliminer ses multiples
        return l
                                
l=cribe_era(200)
m=primes(200)
p=primes(1000)
print(m)
print("\n")
print(l)

with open('primes.txt', 'w') as fichier:
        cpt = 0
        for i in range(len(p)):
                fichier.write('{:5d} '.format(p[i]))
                cpt = cpt + 1
                if cpt>9:
                         fichier.write('\n')
                         cpt=0
N = 10
#legend_fonct = ['pi_primes', 'n_logn']
#blue_line = mlines([], [], color='blue', marker='*',
#                          markersize=15, label='Blue stars')
for i in range(2, N+1):
        plt.title(r'$\pi(n) \ et \ \frac{n}{\log{n}}\ avec\ 1 \leqslant n \leqslant$'+"{:d}".format(N))
        plt.scatter(i,len(primes(i)), color='green', marker='.', linewidth=0.3)
        if np.log(i)!=0:
                plt.scatter(i,i/(np.log(i)) , color='red', linewidth=0.8)
plt.grid()
#plt.legend(handles=[blue_line])
plt.savefig('n_10.png')
plt.show()
### la création du fichier txt prend pas mal de temps donc nous l'avons mis
## en commentaire.
"""
with open('table.txt', 'w') as fichier:
        fichier.write('{:7s} | {:6s} | {:10s}\n'.format('n', ' pi(n)',' n/log(n)'))
        for i in range(1,7):
                fichier.write('{:7d} | {:6} | {:10}\n'.format(10**i,len(primes(10**i)), 10**i/np.log(10**i)))
"""                

