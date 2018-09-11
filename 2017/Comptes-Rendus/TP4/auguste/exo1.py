from math import *


def is_prime(n):
	if n%2==0:
	    return False
	else:
	    if n==0 or n==1 :
	        return False
	    else :
	        i = 3
		while i <= sqrt(n):
			if n%i == 0 :
				return False
			else :
				i = i+1
		return True

l = is_prime(1000)
print l
