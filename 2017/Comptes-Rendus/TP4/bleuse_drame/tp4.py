from random import *
from math import log

###Exercice 1

#a
a=10
b=3
print(a/b) #Quotient
print(a%b) #Reste

#d

def is_prime(n):
	i = 1
	for k in range (2,n):
		i=n%k
		if i == 0:
			return False
	return True

#test:

r = is_prime(4294997)
print r

###Exercice 2

#b

def primes(n):
	a=1
	L=[]
	for i in range(2,n+1):
		for k in range(2,i):
			a=i%k
			if a!=0:
				L.append(i)
	return L

r=primes(9)
print r


def primes(n):
	L = []
	for i in range(2, n+1):
		if is_prime(i):
			L.append(i)
	return L

n = 1000
list_premiers = primes(n)
print list_premiers

#d

N = 100
nn = range(2, N)

gn = [n/log(n) for n in nn]
pin = [pi(n) for n in nn]

plt.clf()

plt.plot(nn, pin, 'r-', nn, gn, 'b')
plt.grid('on')
plt.axis('equal')
plt.savefig('graph2.png')

#e

n='n'
d='pi(n)'
t='n/log n'

print('{0:10}|{1:10}|{2:10}'.format(n,d,t))

"""
t='---------------------------------------------------------------------------------'
print(t)
for i in range(1,6):
	p=10**i
	V=pi(p)
	g=p/log(p)
	print('{0:10}|{1:10}|{2:10}'.format(p,V,g))
"""
##Exercice 3
def factors(n):
	Primes = primes(n)
	FF = []
	for p in Primes:
		while n%p == 0:
			n = n/p
			FF.append(p)
	return FF


##Exercice 4

def euclide (a,b):
	r,u,v = a,1,0
	rp,up,vp = b,0,1
	while rp != 0:
		q = r//rp
		rs,us,vs = r,u,v
		r,u,v = rp,up,vp
		rp,up,vp = (rs-q*rp), (us-q*up), (vs-q*vp)
	return (r,u,v)

##Exercice 5

#b


