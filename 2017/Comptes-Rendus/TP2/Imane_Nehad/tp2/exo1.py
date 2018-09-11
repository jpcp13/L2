def f(x):
	return 1-x**2

x, dx = -0.5, 0.001
X, Y, Points = [], [], []

while x <= 0.5:
    y = f(x)
    point = (x, y) 
    X.append(x) 
    Y.append(y) 
    Points.append(point) 
    x += dx

import matplotlib.pyplot as plt 
plt.plot(X, Y, 'r')
plt.grid()
plt.show()
