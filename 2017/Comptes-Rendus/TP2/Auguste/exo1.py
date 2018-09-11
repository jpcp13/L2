def f(x):
	import numpy as np
	return np.sqrt(1-x**2)

x = -0.5
dx = 0.1
X, Y, Points = [], [], []

while x < 0.5 :
	y = f(x)
	point =(x, y)
	X.append(x)
	Y.append(y)
	Points.append(point)
	x= x+dx
print(X)
print(Y)

plt.plot(X, Y, '*r')
plt.grid()
plt.show()
