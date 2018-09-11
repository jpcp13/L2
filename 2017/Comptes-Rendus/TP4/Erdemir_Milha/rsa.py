import numpy as np
import random
import fonctiontp4 as f
#exo 5
#a.Fonctionnement du chiffrement RSA vu.
#b.
x = False
while not x:
	n = random.randint(2**35, 2**36)
	print n
	x = f.is_prime(n)


p = 48325293571
q = 55566605723
n = p*q
e = 29
#c 
"n est trop grand donc python ne peut pas l executer avec is_prime"

#d 
"fi(n)= fi(p)*fi(q)*pgcd(p,q)/fi(pgcd(p,q)) ici pgcd(p,q) = fi(pgcd(p,q)) = 1 car p et q sont premiers donc sont premiers entre eux. On en deduit que fi(n) = fi(p)fi(q) = (p-1)(q-1)"


#e
"On choisit e = 29."

#f
"# on utilse euclide"

u = f.euclide(29,48325293570*55566605722)

"On trouve avec le terminal u = -1018551650905000340791 et v = 11)
