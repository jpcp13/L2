"""
### Methode
"""
import time

def point_milieu(f, a, b, n):
	t = time.clock()
	pas = abs(b - a)/n
	somme = 0
	for i in range(n):
		somme = somme + pas * f(a+i*pas+pas/2)
	return somme, time.clock()-t

def trapeze(f, a, b, n):
	t = time.clock()
	pas = abs(b - a)/n
	somme = 0
	for i in range(n):
		somme = somme + pas * (f(a + i*pas) + f(a + (i+1)*pas))/2
	return somme, time.clock()-t
	
def simpson (f, a, b, n):
    t= time.clock()
    pas= abs(b-a)/n
    somme1=0
    somme2=0
    somme3=0
    for i in range(0,n/2-1):
        somme1 = somme1 + (f(a+pas*2*(i+1)))
    for j in range(0,n/2):
        somme2 = somme2 + (f(a+pas*2*(j+1)-pas))  
    somme3 = (pas/3)*(f(a)+f(b)+2*somme1 + 4*somme2)
    return somme3, time.clock()-t
