from methods import *


x = np.linspace(0, 2, 100)
y = u(x)
y2 = u2(x)
y3 = u3(x)

suite, xsuite = euler(f, 1, 2, 20)
suite2, xsuite2 = euler(f2, 1, 2, 20)
suite3, xsuite3 = euler(f, 1, 1, 30)
plt.scatter(xsuite, suite)
plt.scatter(xsuite2, suite2)
plt.scatter(xsuite3, suite3)
plt.plot(x,y)
plt.grid()
#plt.show()
plt.savefig('suite')



