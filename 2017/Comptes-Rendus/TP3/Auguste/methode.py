
def dichotomie(f,a,b,epsi):
    g,d = a,b
    while (d-g) > 2*epsi :
        m = (d+g)/2
        if (f(g)*f(m)) <= 0 :
            d = m
        else :
            g = m
    return (d+g)/2


def point_fixe(g, X0, epsi):
    x = X0
    N = 2*epsi
    while N > epsi:
        x1 = g(X0)
        N = abs(x1-x)
        x = x1
	print x
    return x


def newton(f,df,x0,epsi):
    x = x0
    y = x0 - f(x0)/df(x0)
    while abs(y-x) >= epsi:
        x = y
        y = y - f(y)/df(y)
    return y

def point_milieu(f,a,b,n):
	somme = 0
	h =  (b-a)/float(n)
	z = 0
	i=1
	while i <= n:
		z = z+h*f(a+i*h)
		i = i+1
	return z

def enregistrer(methode,func,string,a,b,n):
	with open('tableau_{:s}.txt'.format(string), 'w') as fichier :
		print('{0:12s} | {1:9s} |  {2:s}'.format(' erreur', 'temps(sec)', 'n'))
		fichier.write('{0:15}|{1:12s}|{2:s}\n'.format('erreur','temps(sec)','n'))
		for j in range(1, n+1):
			integrale,temps = methode(func,a,b,10**j)
			erreur = abs(integrale - I)
			print('{0:e} | {1:e} | {2:d}' .format(erreur, temps, 10**j))
			fichier.write('{0:9e} | {1:e} | {2:d}\n' .format(erreur,temps, 10**j))
	print('')

def trapezes(f,a,b,n) :
	h=(b-a)/float(n)
	z=0.5*(f(a)+f(b))
	for i in range(1,n) :
		z=z+f(a+i*h)
	return h*z

def Simpson(f,a,b,n) :
	h=(b-a)/float(n)
	z=(f(a)+f(b))/6
	for i in range(1,n) :
		z=z+f(a+i*h)/3
	for i in range(n) :
		z=z+f(a+(2*i+1)*h/2)*2/3
	return h*z


def Monte_Carlo(N):
	R1, R2 =[],[] 
	V1, V2 =[],[] 

	I = 0   
	E = 0	

	for i in range (N):
		x = rd.uniform(-1, 1)
		y = rd.uniform(-1, 1)

		if (x*x + y*y) <= 1:
			R1.append(x)
			R2.append(y)
			I += 1
		else:
			V1.append(x)
			V2.append(y)
			E += 1
	return I/N
