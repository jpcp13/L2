from fonctions import * 
from math import * 

# Question 1 e) 

show = 0 
for i in range(0,5):
	if is_prime(Fermat(i)) == True: 
		show = 'le nombre F('+repr(i)+') est premier'
	else: 
		show = 'le nombre F('+repr(i)+') n est pas premier'
	print(show)
