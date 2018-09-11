import numpy as np

# Definition de fonction

def is_prime(n):
	n = int(np.sqrt(n))
	for i in range(2,n):
		if(n % i == 0):
			return False
	return True

#Chiffrement RSA

low = 2**35
high = 2**36
p = np.random.randint(low, high)
while (not is_prime(p)):
	p = np.random.randint(low, high)

q = np.random.randint(low, high)
while ( (not is_prime(q)) or p == q):
	q = np.random.randint(low, high)
	

print "p :",p
print "q :",q

