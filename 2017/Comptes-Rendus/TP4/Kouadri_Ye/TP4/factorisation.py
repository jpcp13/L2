from prime import *	

n=60

def factor(n):
	liste=[]
	k=n
	l=primes(n)
	for i in range (len(l)):
		if k%l[i]==0:
			while(k!=1 	and k%l[i]==0):
					k=(k/l[i])
					liste.append(l[i])
	return liste


print(factor(924))

