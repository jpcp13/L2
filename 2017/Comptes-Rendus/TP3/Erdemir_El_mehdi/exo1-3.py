import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def f(x):
    return np.exp(-x)

x=0
dx=0.1
X,Y,Points=[],[],[]

while x<=2.1 :
    y=f(x)
    point=(x,y)
    X.append(x)
    Y.append(y)
    Points.append(point)
    x=x+dx
print(X)
print(Y)

plt.plot(X, Y, '*r')
plt.grid()
plt.show()
