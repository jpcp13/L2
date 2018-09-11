#Mouhamadou Moustapha Gueye
#Lynda Hedir

import matplotlib.pyplot as plt
import numpy as np

#Exercice 1
#c) Creation de la fonction u(t)
 
def f(x):
        return np.exp(-x)
    
#Representation graphique de u

x=np.linspace(0,2,100) #creation de l'abscice x
y=[f(i) for i in x] #creation de l'ordonnee y
plt.plot(x,y)
plt.grid()
plt.legend(["f=exp(-x)"])

