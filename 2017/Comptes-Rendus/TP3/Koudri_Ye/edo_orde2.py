import matplotlib.pyplot as plt
import numpy as np

n=300 #precision

def U(u,v):
        return np.array([u, v]) #retourne un objet de type array

def F(t, U):
        return np.array([U[1], -U[0]])

def Euler(F, U0, T, n):
        h = (float(T)/n)
        tt=np.linspace(0, T, n+1)
        suite= [U0]
        for i in range(0, n):
                U0=U0+h*F(h*i, U0)
                suite.append(U0)
        UU=np.asarray(suite) #convertir une liste en array
        return tt,UU


tt, UU= Euler(F, U(1,0), 4*np.pi, n)

x= np.linspace(0,4*np.pi,100)
y=np.cos(x)

# equation differentielle
plt.title('u en fonction du temps')
plt.plot(x, y, color='red', linewidth=0.8, label = r"$f(x) = cos(x)$")
plt.scatter(tt, [UU[i][0] for i in range(n+1)], color='green', marker='.', linewidth=0.3)
"""
# [UU[i][0] for i in range(n)] : une liste de valeurs
# valeur du premier element de chaque element de UU c-a-d les valeurs de u
# En faisant varier i on accede a chaque element de UU c-a-d U
"""
plt.grid()
plt.legend()
plt.savefig('u_ft.png')
plt.show()



plt.title('v en fonction du temps')
plt.plot(x, -np.sin(x), color='red', linewidth=0.8, label=r"$f(x) = - sin(x)$")
plt.scatter(tt, [UU[i][1] for i in range(n+1)], color='green', marker='.', linewidth=0.3)
plt.grid()
plt.legend()
plt.savefig('v_ft.png')
plt.show()

plt.title('v en fonction de u')
plt.plot(np.cos(x), np.sin(x), color='red', linewidth=0.8, label = r"$x^2 + y^2 = 1$")
plt.scatter([UU[i][0] for i in range(n+1)], [UU[i][1] for i in range(n+1)], color='green', marker='.', linewidth=0.3)
plt.grid()
plt.legend()
plt.savefig('v_fu.png')
plt.show()
