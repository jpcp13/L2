from methods import *
"""
def euler_2(F, U0, T, n):
	h = (float(T)/n)
	UU = np.zeros((2, n+1))
	U = U0
	t = 0.0
	for i in range(n+1):
		UU[:, i] = U #i eme colonne de UU
		U = U + h*F(t, U)
		t = t + h

	tt = np.linspace(0, T, n)
	return UU, tt
"""




U0 = 1,0
n = 4
def euler_2(F, U0, T, n):
	h = (float(T)/n)
	tt = tt = np.linspace(0, T, n+1)
	suite = [U0]
	for i in range(0, n):
			U0 = U0 + h*F(h*i, U0)
			suite.append(U0)
	UU = np.asarray(suite)
	return tt, UU




T = 4*pi
U0 = 1,0
n = 4
tt, UU = euler_2(F, U0, 4*np.pi, n)
#test = euler_2(F, U0, T, n) 
print tt, UU


"""
#test = euler_2(F, U0, T, n) 

x = np.linspace(0, T, 100)
y = np.cos(x)

plt.title('u en fonction du temps')
plt.plot(x, y, color='red', linewidth= 0.8, label= r"$f(x) = cos(x)$")
plt.scatter(tt, [UU[i][0] for i in range(n+1)], color='green', marker='.', linewidth=0.3)
"""




















