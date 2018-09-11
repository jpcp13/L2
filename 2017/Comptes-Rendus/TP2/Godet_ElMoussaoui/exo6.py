import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import math

circle1 = plt.Circle((0, 0), 1, color='r')


fig, ax = plt.subplots() 
# note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

# change default range so that new circles will work
ax.set_xlim((-5,5))
ax.set_ylim((-5,5))

ax.add_artist(circle1)
plt.grid('on')
plt.show()


# [0;1]
for i in range(5):
	rand = np.random.rand()
	print rand,"\n"

# [-1;1]
for j in range(5):
	randn = 2*np.random.rand()-1
	if randn > 1:
		randn = cos(randn)
	print randn,"\n"



