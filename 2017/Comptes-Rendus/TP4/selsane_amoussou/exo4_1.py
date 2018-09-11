
import numpy as np
from tp4 import *

#a) voir fichier odt
#b) voir fichier odt
#c) voir fichier odt	
#d) voir fichier tp3.py
#e)
FF = np.zeros(6)
for k in range(6) :
	FF[k] = 2**(2**k)
	p = is_prime(FF[k])
	print(p)
