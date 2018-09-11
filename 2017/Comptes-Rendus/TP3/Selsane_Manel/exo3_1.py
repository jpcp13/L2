#Exercice 1


from tp3 import*

#c) 
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2,10)
plt.plot(t,u(t),'r-') 
plt.grid('on')
plt.axis('equal')
plt.savefig('graphU.png')

