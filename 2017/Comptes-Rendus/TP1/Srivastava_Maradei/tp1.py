

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
	cppointfixe = 0
	x=x0
	delta=2*epsi
	while delta >= epsi:
		cppointfixe += 1
		x1=g(x)
		delta = abs(x1-x)
		x=x1
	return cppointfixe


xo=1.0
epsi=1e-12
#~ v=h(g,1.0,epsi)
#~ print(r)
#~ print(g(r))


#Exo 4

def newton(h, dh, x0, epsi):
	cpnewton = 0
	r=x0
	i = 1
	while i == 1:
		cpnewton += 1
		#print(r)
		prec = r
		r=r-(h(r)/dh(r))
		if abs(r-prec)<epsi: 
			i = 0
	return r, cpnewton



w = newton(h, dh, 1.0, 1e-12)


#exo5

def secantes(f, x0, x1, epsi):
	cpsecantes = 0
	s=x1
	r=x0
	i=1
	prec2=r
	prec1=s
	while i == 1:
		cpsecantes += 1
		num = prec1 - prec2
		den = f(prec1)-f(prec2)
		r = prec1 - num/den*f(prec1)
		prec2 = prec1
		prec1 = r
		if abs(r-prec2) < epsi:
			i=0  
	return r, cpsecantes 

r = secantes(f, 1.5, 2.0, 1e-12)

#exo6

def dichotomie(f, a, b, epsi):
	i=1
	cpdichotomie = 0

	while i == 1: 
		cpdichotomie += 1
		if(f(a)>0 and f((a+b/2)>0) or (f(a) < 0 and f((a+b)/2)<0)):
			a = (a+b)/2
		else:
			b = (a+b)/2
		if abs(b-a)<epsi:
			i = 0 
		point = (a,b)
	return point, cpdichotomie	

#~ a = dichotomie(j,1.5,2.0,1e-12)

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

















