from math import *
from pylab import *
from fonctions import *

###### Exercice 1 ######

x = linspace(-0.5, 0.5)
y = f(x) 
plot(x, y)
grid()
xlim(-0.5, 0.5)
title("Fonction f(x)")

show()
