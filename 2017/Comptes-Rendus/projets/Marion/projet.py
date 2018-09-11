from math import *

def bindec(n):
    if n<10:
        return n
    else:
        return 2*bindec(n/10)+n%2
 
liste = [1010, 1101, 0100, 1001, 0011, 1110, 1100, 0110]

i=0

for i in range (len(liste)-1) :
	
	bindec(liste[i])
