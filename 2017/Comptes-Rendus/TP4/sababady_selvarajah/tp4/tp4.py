#SABABADY Kamala
#SELVARAJAH Dinusan

from math import sqrt

def is_prime(n):
	
	if(n == 1 or n == 0):
		return False
	if(n == 2):
		return True
	else:
		i = 2	
		verif = 1

		while i <= sqrt(n):
        		if n % i == 0:
            			verif = 0
            			break
       			else:
            			i = i + 1
     
    	if verif == 0:
        	return False
    	else:
        	return True

def primes(n):
	return [i for i  in range (2,n+1) if is_prime(i)]

def pi(n):
	L = primes(n)
	verif = len(L)
	return verif


def factors(n):
	F = []
	if n == 1:
		return F
	while n >= 2:
        	x,r = divmod(n,2)
        	if r!=0:
            		break
        	F.append(2)
        	n = x
    	# recherche des facteurs 1er >2
    	i=3
    	rn = sqrt(n)+1
    	while i<=n:
       	 	if i>rn:
           	 	F.append(n)
            		break
        	x,r = divmod(n,i)
        	if r == 0:
            		F.append(i)
            		n = x
            		rn = sqrt(n)+1
       		else:
            		i += 2
    	return F

def factors1(n):
	F = []
	i = 2
	while n>1:
		while n%i == 0:
			n = n/i
			F.append(i)
			
		i += 1
	return F



def euclide(a, b):
    d, x, y = a, 1, 0
    dp, xp, yp = b, 0, 1
    while dp != 0:
        q = d//dp
        ds, xs, ys = d, x, y
        d, x, y = dp, xp, yp
        dp, xp, yp = (ds - q*dp), (xs - q*xp), (ys - q*yp)

    return (d, x, y)



