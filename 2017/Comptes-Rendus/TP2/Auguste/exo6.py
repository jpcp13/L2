from matplotlib import pyplot as plt

#6a)
plt.plot([-1,1],[-1,1],'k-')
fig = plt.gcf()
circle=plt.Circle((0,0),1,linewidth=1,facecolor='w',edgecolor='k')
plt.text(0,0,'O',color='r')
fig.gca().add_artist(circle)
plt.grid()
plt.show()

#6b)
from math import *
import numpy as np
print('valeurs aleatoires:')
print(np.random.rand(10))


print('valeurs aleatoires entre -1 et 1:')
print(np.random.uniform(-1,1,10))

#6f)
l = Monte_Carlo(N)
print l
