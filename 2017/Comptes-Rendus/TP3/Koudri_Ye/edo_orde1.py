import matplotlib.pyplot as plt
import numpy as np

n_d = 30 #Nombre de division

####### u'(x) = -u(x)
def u(x):
        return np.exp(-x)
def f(t, u):
        return -u

####### u'(x) = -u(x) + x
def u2(x):
        return 2*np.exp(-x)+x-1
def f2(t, u):
        return -u+t
        
####### u'(x) = (u(x))^2
def u3(x):
        return -1 / (x-1)
def f3(t, u):
        return u**2

####### u'(x) = (u(x))^2 - x
def f4(t, u):
        return u**2 - t

#######

def Euler(f, u, T, n):
        h = (float(T)/n)
        suite =[u]
        for i in range(0, n):
                u=u+h*f(h*i, u)
                suite.append(u)
        uu=np.asarray(suite) #convertir une liste en array
        tt=np.linspace(0, T, n+1)
        return uu, tt


suite, xsuite = Euler(f, 1, 2, n_d)
suite2, xsuite2 = Euler(f2, 1, 2, n_d)
suite3, xsuite3 = Euler(f3, 1, 1, n_d)
suite4, xsuite4 = Euler(f4, 1, 1, n_d)

#####-Affichage-#####

## question 2a: affichage des n+1 valeurs de uk+1 avec la méthode d'Euler
## en prenant T=2 et n=10, f(tk, uk)=-uk.
h=(float(2)/10)
test=1
s='question 2.a: les valeurs des n+1 premiers termes de la suite uk'
Y=[1]
print(s)
for i in range(1, 12):
        test=test+h*(-test)
        if (i<11):
                 Y.append(test)
        s='u'+repr(i)+'= '
        print(s, end='')
        print(test),\
               
Y2=np.asarray(Y)
tt=np.linspace(0, 2, 11)
## On obtient le meme résultat si on applique Euler a f avec n_d=10
test1, test2= Euler(f,1,2,10)
print(tt)
print(Y2)


x = np.linspace(0, 2, 100)
y = u(x)
y2 = u2(x)
y3 = u3(x)

plt.title(r"$u'(t) = -u(t)$")
plt.plot(x,y , color='red', linewidth=0.8, label=r"$u(t) = e^{-t}$")
plt.grid()
plt.legend()
plt.savefig("u1.png")
plt.show()

plt.title(r"$u'(t) = -u(t)$")
plt.plot(x,y , color='red', linewidth=0.8, label=r"$u(t) = e^{-t}$")
plt.scatter(tt, Y2, color='green', marker = 'x', linewidth=0.3)
plt.text(1, .6, "{:d} subdivisions".format(10), color='green')
plt.grid()
plt.legend()
plt.savefig("u1_"+"{:d}".format(10)+".png")
plt.show()

plt.title(r"$u'(t) = -u(t)$")
plt.plot(x, y, color='red', linewidth=0.8, label=r"$u(t) = e^{-t}$")
plt.scatter(xsuite, suite, color='green', marker = 'x', linewidth=0.3)
plt.text(1, .6, "{:d} subdivisions".format(n_d), color='green')
plt.grid()
plt.legend()
plt.savefig("u1_"+"{:d}".format(n_d)+".png")
plt.show()

# u'(x) = -u(x) + x
plt.title(r"$u'(t) = -u(t) + t$")
plt.plot(x, y2, color='red', linewidth=0.8, label=r"$u(t) = 2 e^{-t} + t - 1$")
plt.scatter(xsuite2, suite2, color='green', marker = 'x', linewidth=0.3)
plt.text(.75, 1, "{:d} subdivisions".format(n_d), color='green')
plt.grid()
plt.legend()
plt.savefig("u2_"+"{:d}".format(n_d)+".png")
plt.show()

# u'(t) = (u(t))^2
plt.title(r"$u'(t) = u^2(t)$")
plt.plot(x, y3, color='red', linewidth=0.8, label=r"$u(t) = - \frac{1}{t - 1}$")
plt.scatter(xsuite3, suite3, color='green', marker = 'x', linewidth=0.3)
plt.text(1.25, 50, "{:d} subdivisions".format(n_d), color='green')
plt.grid()
plt.legend()
plt.savefig("u3_"+"{:d}".format(n_d)+".png")
plt.show()

# u'(t) = (u(t))^2 - t
plt.title(r"$u'(t) = u^2(t)-t$")
plt.scatter(xsuite3, suite3, color='green', marker = 'x', linewidth=0.3)
plt.text(0.9, 2, "{:d} subdivisions".format(n_d), color='green')
plt.grid()
plt.legend()
plt.savefig("u4_"+"{:d}".format(n_d)+".png")
plt.show()
