import numpy as np
from module import *

FF = np.zeros(6)
for k in range(6):
	FF[k] = 2**(2**k)
	p = is_prime(FF[k])
	print(p)
