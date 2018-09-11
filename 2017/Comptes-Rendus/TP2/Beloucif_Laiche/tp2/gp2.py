import numpy as np 
from math import *
from time import *
from tp2 import *
import matplotlib.pyplot as plt

teta = np.linspace(0, 2*np.pi, 100)

x = np.cos(teta)
y = np.sin(teta)

plt.plot(x, y)
plt.grid()
plt.savefig('cercle.png')
