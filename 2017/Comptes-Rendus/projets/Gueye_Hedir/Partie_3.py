import matplotlib.pyplot as plt
from Partie_1 import *


#Commande pour croiser des variables

print(pd.crosstab(frame['year'],frame['state']))


#Commande pour tracer l'histogramme

frame.hist(column='year')

axes = plt.gca()

axes.xaxis.set_ticklabels(['', '2000', ' ', ' ',' ', '2001', ' ', ' ', ' ', '2002'])


#Commande pour tracer le nuage de points

frame.plot.scatter(x='year',y='pop')


axes = plt.gca()

axes.xaxis.set_ticklabels(['', '2000', ' ', ' ',' ', '2001', ' ', ' ', ' ', '2002'])
