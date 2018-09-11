
#Partie 4: Newton

def newton(f,df,x0,epsi):
    d=2*epsi
    x=x0
    compt=0
    nbiter=0
    while d> epsi and compt< 48:
            compt+=1
            v=x-(f(x)/df(x))
            x=v
            print('x = {0}, compteur ={1}\n').format(x,compt)
    print('Le nombre diteration est ={0}').format(compt)
    return v, nbiter
#4.d)
    
#Test 1
print("\n")
n="Test 1 NEWTON"
print(n)
print("\n")

def f(x):

	return x**2-x -1

def df(x):
        return 2*x-1.0
    
x0=1.0
epsi=1e-12
r, nbiter = newton(f,df,x0,epsi)
print("\n")

#Test 2
n2=" Test 2 NEWTON"
print(n2)
print("\n")
                
x0=-1.0
epsi=1e-12
r, nbiter = newton(f,df,x0,epsi)
print("\n")



