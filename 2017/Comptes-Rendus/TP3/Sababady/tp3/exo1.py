#SABABADY Kamala
#SELVARAJAH Dinusan
import math
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 2, 100)
plt.plot(x, np.exp(-x),'b-')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f=exp(-x)"])
plt.axis("equal")
plt.grid()
plt.savefig('1.png')


