
from numpy import *
from matplotlib.pyplot import *
def f(x):
    return x**2-x-1
x=linspace(-1.,2.,100)
plot(x,f(x))
show()


def g(x):
    return 1+(1/x)

x=linspace(-1.,2.,30)
plot(x,g(x))
show()

x=linspace(-1., 2., 30)
plot(x, f(x))
plot(x, g(x))
show()

X0=1.0
XX=[X0]
for i in range(25):
    X1=g(X0)
    XX.append(X1)
    X0=X1
    print(X0)
print(XX)

#2.0
1.5
1.66666666667
1.6
1.625
1.61538461538
1.61904761905
1.61764705882
1.61818181818
1.61797752809
1.61805555556
1.61802575107
1.61803713528
1.61803278689
1.61803444782
1.6180338134
1.61803405573
1.61803396317
1.61803399852
1.61803398502
1.61803399018
1.61803398821
1.61803398896
1.61803398867
1.61803398878
[1.0, 2.0, 1.5, 1.6666666666666665, 1.6, 1.625, 1.6153846153846154, 1.619047619047619, 1.6176470588235294, 1.6181818181818182, 1.6179775280898876, 1.6180555555555556, 1.6180257510729614, 1.6180371352785146, 1.6180327868852458, 1.618034447821682, 1.618033813400125, 1.6180340557275543, 1.6180339631667064, 1.6180339985218035, 1.618033985017358, 1.6180339901755971, 1.6180339882053252, 1.6180339889579018, 1.6180339886704433, 1.6180339887802426]

def point_fixe(g,x0,epsi):
    x=x0 
    delta=2*epsi
    while delta>epsi:
        x1=g(x) 
        delta=abs(x1-x)
        x=x1
    return x 

x0= -0.6
epsi=1e-12
r=point_fixe(g,x0,epsi)
print r
print g(r)


def f(x):
    return x**2-x-1

def df(x):
    return 2*x-1

def g(x):
    return 1/1+x

def h(x):
    return x-f(x)/df(x)


def newton(f,df,x0,epsi):
    """" Entrees : f fonction , df sa derivee et x0 premiere estimation
                     prec precision(=epsilon)
         Sorties : x estimation de c une solution de f (x )=0 """
    x=x0
    delta=2*epsi
    while delta>epsi:
        x1=x-f(x)/df(x)
        delta=abs(x1-x)
        x=x1
        print x
    return x

x0=-1.0
epsi=1e-12
r=newton(h,x0,epsi)
print('r={0}'.format(r))
print('g(r)={0}'.format(g(r)))

print("\n")



def f(x):
    return x**2-x-1


def dichotomie(f,a,b,epsi):
    err=abs(b-a)
    if f(a)*f(b)>0:
        return 'Il_faut_choisir_un_autre_intervalle'
    else:
        while err > epsi:
            c=0.5*(a+b);
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            err=0.5*err
        return c


a=-1.0
b=0.0
epsi=1e-12
t=dichotomie(f,a,b,epsi)
print t



    



def point_fixe(g,x0,epsi):
    x=x0 
    delta=2*epsi
    nbiter2=0
    while delta>epsi:
        x1=g(x) 
        delta=abs(x1-x)
        x=x1
    r=x
    return r, nbiter2





def newton(h,x0,epsi):
    delta=2*epsi
    nbiter2=0
    while delta>epsi:
        nbiter2 +=1
        x1=h(x0)
        delta=abs(x1-x0)
        x0=x1
    r=x0
    return r,nbiter2


def secante(f,x0,x1,epsi):
    delta=2*epsi
    nbiter3=0
    while delta>epsi:
        nbiter3+=1
        num= x1-x0
        den=h(x1)-h(x0)
        x2=x1-(num/den)*f(x1)
        delta=abs(x2-x1)
        x0=x1
        x1=x2
    t=x1
    return t, nbiter3

def dichotomie(f,a,b,epsi):
    g=a
    d=b
    nbiter4=0
    while (d-g)>2*epsi:
        nbiter4=nbiter4+1
        m= (d+g)/2
        if (f(g)*f(m))<= 0:
            d=m
        else:
            g=m
    return (d+g)/2, nbiter4

#tests
print("\nTest Point fixe \n")
r, nbiter1=point_fixe(g,1.0,1e-15)
print "Nombre d'iteration :",nbiter1
print "r :  ",r
print "g(r):",g(r)



print("\Test Secante \n")
r2, nbiter3=point_fixe(h,1.5,2,1e-15)
print "Nombre d'iteration :",nbiter3
print "r :  ",r2
print "h(r):",h(r)

print("\nTest dichotomie \n")
r3, nbiter4=point_fixe(f,1.5,2.0,1e-15)
print "Nombre d'iteration :",nbiter4
print "r :  ",r3
print "f(r):",f(r3)

print("\nTest Newton \n")
r1, nbiter2=point_fixe(f,1.0,1e-15)    
print "Nombre d'iteration :",nbiter2
print "r :  ",r1
print "f(r):",f(r)

