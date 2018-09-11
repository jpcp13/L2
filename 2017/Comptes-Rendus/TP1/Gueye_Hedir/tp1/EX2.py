#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:35:56 2017

@author: 11608524
"""
#Partie 2 : 1+ 1/x
 
#2.a)

import matplotlib.pyplot as plt
def g(x):

	return 1+ 1/x
import numpy as np
t=np.arange(1.5, 2.0 ,0.01)
plt.plot(t, g(t),'r-', t, t, 'b')
plt.grid('on')
plt.axis('equal')
plt.show()



#2.b)

x0=1.0
nx=[x0]
for i in range(25):
	x1=g(x0)
	nx.append(x1)
	x0=x1

print (x0)
print (nx)
print ("\n")
