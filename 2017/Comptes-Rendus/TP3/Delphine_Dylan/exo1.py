import numpy as np
import matplotlib.pyplot as plt
from math import *
from moduletp3 import *


def u(t):
	return np.exp(-t)

t = np.linspace(0. , 2. , 1000);
plt.plot(t , u(t), 'r')
plt.axis([0, 2, 0, 1])
plt.grid()
#plt.show()
plt.savefig('graphiquedef')


