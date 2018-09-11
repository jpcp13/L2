# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

#Exercice 1
#a) Création de la fonction f(x)
 
def f(x):
        return math. sqrt(1-x**2)
    
#Representation graphique de f(x)

x=np.linspace(-0.5,0.5,30) #création de l'abscice x
y=[f(i) for i in x] #creation de l'ordonnee y
plt.plot(x,y)
plt.grid()
plt.show