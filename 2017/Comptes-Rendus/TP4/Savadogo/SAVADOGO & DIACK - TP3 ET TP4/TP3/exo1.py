from methods import *


#Representation graphique de la fonction exp
x = np.linspace(0, 2)
y = np.exp(-x)
plt.xlim(0, 2)
plt.plot(x, y)
plt.grid()
#plt.show()
plt.savefig('exp(-x)')
