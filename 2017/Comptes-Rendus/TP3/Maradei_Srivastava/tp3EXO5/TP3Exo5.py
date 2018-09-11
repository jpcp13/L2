import matplotlib.pyplot as plt
import numpy as np

n=300 #precision

def U(u,v):
	return np.array([u, v]) #retourne un objet de type array

def F(t, U):
	return np.array([U[1], -U[0]])

def Euler(F, U0, T, n):
	h = (float(T)/n)
	tt=np.linspace(0, T, n)
	suite= []
	for i in range(0, n):
		suite.append(U0)
		U0=U0+h*F(h*i, U0)
	UU=np.asarray(suite) #convertir une liste en array
	return tt,UU


tt, UU= Euler(F, U(1,0), 4*np.pi, n)

x= np.linspace(0,4*np.pi,100)
y=np.cos(x)

# equation differentielle
plt.title('u en fonction du temps')
plt.plot(x, y, color='red', linewidth=0.8, label = r"$f(x) = cos(x)$")
plt.scatter(tt, [UU[i][0] for i in range(n)], color='green', marker='.', linewidth=0.3)
"""
# [UU[i][0] for i in range(n)] : une liste de valeurs
# valeur du premier element de chaque element de UU c-a-d les valeurs de u
# En faisant varier i on accede a chaque element de UU c-a-d U
"""
plt.grid()
plt.legend()
plt.savefig('u_ft.png')
plt.show()



