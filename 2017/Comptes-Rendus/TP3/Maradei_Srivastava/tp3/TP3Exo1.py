from pylab import * 
from math import *
from methodes import *
	
x = linspace(0, 2) 
y = u(x) 
plot (x,y)
grid()

xlim(0, 2)
title("Fonction exo1")
show()	
plt.savefig()
	
