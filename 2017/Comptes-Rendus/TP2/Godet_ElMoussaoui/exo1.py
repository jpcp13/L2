# Definition de fonction



def f(x) :
	import numpy as np	
	return np.sqrt(1 -x*x)


# Graphes

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-0.5, 0.5, 0.1)
plt.plot(x, f(x),'r-')
plt.grid('on')
plt.axis('equal')
plt.show()

