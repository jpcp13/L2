import numpy as np
import matplotlib.pyplot as plt
import time
import math

def f(x):
	return np.sqrt(1-x**2)


x = np.linspace(-0.5, 0.5, 10) # j'ai rajouté np.
plt.plot(x, f(x))
plt.grid()
plt.show()

