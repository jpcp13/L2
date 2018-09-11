from math import sqrt

def is_prime(n) : 
	if n==0 or n==1 :
		return False 
	if n == 2: 
		return True
	else :
		i = 2
		k = 1
		while i<= sqrt(n):
			if n % i == 0:
				k = 0
				break
			else :
				i = i+1
	if k == 0 :
		return False
	else :		
		return True

def primes(n) :
	return [i for i in range(2, n+1) if is_prime(i)]

def pi(n) :	
	L = primes(n)
	k = len(L)
	return k


def factors(n):
	Primes = primes(n)
	FF = []
	for p in Primes:
		while n%p == 0:
			n = n/p
			FF.append(p)
	return FF						

"""
def euclide(a, b):
	BB = []
	cpt = 0
	while a%b != 0 and cpt<20:
		a, b = b, a%b
		cpt +=1
		print("a ={0}, b ={1} \n".format(a,b))
		BB.append(b)
	
	return BB


"""

def euclide(a, b):
    d, u, v = a, 1, 0
    dp, up, vp = b, 0, 1
    while dp != 0:
        q = d//dp
        ds, us, vs = d, u, v
        d, u, v = dp, up, vp
        dp, up, vp = (ds - q*dp), (us - q*up), (vs - q*vp)

    return (d, u, v)
