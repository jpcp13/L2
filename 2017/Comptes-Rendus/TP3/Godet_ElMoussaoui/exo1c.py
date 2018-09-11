import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def f(x):
    return sp.e**-x

x = np.arange(0, 2, 0.1)
plt.plot(x, f(x),'r-')
plt.grid('on')
plt.axis('equal')
plt.show()

