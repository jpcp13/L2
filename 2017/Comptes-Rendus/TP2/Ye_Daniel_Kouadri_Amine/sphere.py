import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

##########################################################
phi = np.linspace(0, 2*np.pi, 25)
psi = np.linspace(0, 2*np.pi, 25)
phi, psi = np.meshgrid(phi, psi)
fig = plt.figure()
ax = Axes3D(fig)
X = np.cos(phi) * np.cos(psi)
Y = np.cos(phi) * np.sin(psi)
Z = np.sin(phi)
ax.plot_wireframe(X, Y, Z, rcount=6, ccount=6)

for i in range(1000):
	xpoint=2*np.random.rand()-1
	ypoint=2*np.random.rand()-1
	zpoint=2*np.random.rand()-1
	if (xpoint**2+ypoint**2+zpoint**2)<1:
		ax.scatter(xpoint, ypoint, zpoint, color='red', marker='.')
	else:
		ax.scatter(xpoint, ypoint, zpoint, color='green', marker='.')
plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)
ax.grid()
plt.savefig('sphere.png')

def montecarlo_sphere(n):
    t=time.clock()
    compt=0
    for i in range(n):
        xpoint=2*np.random.rand()-1
        ypoint=2*np.random.rand()-1
        zpoint=2*np.random.rand()-1
        if (xpoint**2+ypoint**2+zpoint**2)<1:
           compt=compt+1
    volume=(compt/float(n)*8)
    return volume, time.clock()-t
    
with open('monte_carlo_sphere.txt', 'w') as fichier2:
    fichier2.write('{0:6s} | {1:s} | {2:s}\n'.format('n', 'erreur', 'temps'))
    for i in range(6):
        volume, temps = montecarlo_sphere(10**i)
        fichier2.write('{0:6d} | {1:f} | {2:f}\n'.format(10**i, abs(volume-(4*np.pi)/3), temps))

