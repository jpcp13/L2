#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS

from module import *

#C.

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2,10)
plt.plot(t,u(t),'r-')
plt.grid('on')
plt.axis('equal')
plt.savefig('graph1.png')

