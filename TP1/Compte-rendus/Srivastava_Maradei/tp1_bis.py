

def f(x):
    return x**2 -x-1

def g(x):
    return 1+(1/x)

def h(x):
	return x**2-x-1

def dh(x):
	return 2*x-1

#################################


  #Exo1
X,Y = [],[]
x=-1

while x <= 2:
    y = f(x)
    X.append(x) 
    Y.append(y) 
    x += 0.25



import matplotlib.pyplot as plt
plt.plot(X, Y, 'b')
plt.grid()
#plt.show()
plt.savefig('fig1.png')

#################################

# Exo 2
Liste = []
n=1


for i in range(25):
    Liste.append(n)
    n= (1 + 1.0/n)
    
print(Liste)

#################################

#EXO 3
           

def point_fixe(g,x0,epsi):
	x=x0
	d=2*epsi
	compt=0
	while d>epsi:
		x1=g(x)
		d=abs(x1-x)
		x=x1
		print (x)
return x


xo=1.0
epsi=1e-12
v=h(g,1.0,epsi)
print(r)
print(g(r))


#Exo 4

def newton(f,df,x0,epsi):
	d=2*epsi
	x=x0
	compt=0
	while d > epsi and compt < 40:
		compt += 1
		v=x-f(x)/df(x)
		x=v
		print('x = {0}, compteur = {1}\n'.format(x,compt))
	return v



w = newton(h, dh, 1.0, 1e-12)


#exo5

def secante(f,x0,x1,epsi):
	delta=2*epsi
	cpt=0
	while delta > epsi and cpt < 100:
		cpt+=1
		num = x1-x0
		delta = abs(num)
		den = f(x1)-f(x0)
		x2=x1-num/den*f(x1)
		x0=x1
		x1=x2
		print('x = {0},compteur = {1}\n'.format(x2,cpt))
	return x2

#exo6

def dichotomie(f, a, b, epsi):
    if b-a<=epsi:
        print(a,b)
        return a,b
    else:
        c=(a+b)/2
        if f(a)*f(c)<=0:
            return dichotomie(f,a,c,epsi)
        else:
	return dichotomie(f,c,b,epsi)	

a = dichotomie(j,1.5,2.0,1e-12)

"""pf3 = point_fixe(f,1.0,1e-3)
pf6 = point_fixe(f,1.0,1e-6)
pf9 = point_fixe(f,1.0,1e-9)
pf12 = point_fixe(f,1.0,1e-12)
pf15 = point_fixe(f,1.0,1e-15)
"""
n3 = newton(h,dh,1.0,1e-3)
n6 = newton(h,dh,1.0,1e-6)
n9 = newton(h,dh,1.0,1e-9)
n12 = newton(h,dh,1.0,1e-12)
n15= newton(h,dh,1.0,1e-15)

s3 = secantes(f, 1.5, 2.0, 1e-3)
s6 = secantes(f, 1.5, 2.0, 1e-6)
s9 = secantes(f, 1.5, 2.0, 1e-9)
s12 = secantes(f, 1.5, 2.0, 1e-12)
s15 = secantes(f, 1.5, 2.0, 1e-15)

a=1.5
b=2.0
d3 = dichotomie(f, a, b, 1e-3)
d6 = dichotomie(f, a, b, 1e-6)
d9 = dichotomie(f, a, b, 1e-9)
d12 = dichotomie(f, a, b, 1e-12)
d15 = dichotomie(f, a, b, 1e-15)

print("10e-3  10e-6  10e-9  10e-12  10e-15")
print(n3,n6,n9,n12,n15)
print(s3,s6,s9,s12,s15)
print(d3,d6,d9,d12,d15)

















