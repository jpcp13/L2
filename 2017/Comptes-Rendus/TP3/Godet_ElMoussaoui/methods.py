# Ce module va contenir des methodes

I =  0.95959077626

def point_fixe(g, x0, epsi): 
    delta = 2*epsi
    nbiter1=0
    while delta>epsi and nbiter1<150:
        nbiter1 += 1
        x1=g(x0)
        delta = abs(x1-x0)
        x0 = x1
    r = x0  
    return r, nbiter1

def newton(h,x0,epsi):
    delta = 2*epsi
    nbiter2 = 0
    while delta>epsi and nbiter2<150:
	nbiter2 += 1
        x1 = h(x0)
        delta = abs(x1 - x0)
        x0 = x1
    r = x0
    return r, nbiter2

def secante(f, x0, x1, epsi):
    delta = 2*epsi
    nbiter3=0
    while delta>epsi and nbiter3<150:
	nbiter3 += 1
        num = x1 - x0
        den = f(x1)-f(x0)
        x2 = x1 - (num/den)*f(x1)
        delta = abs(x2 - x1)
        x0=x1
        x1=x2
    t = x1
    return t, nbiter3
   
def dichotomie(f, a, b, epsi):
    g = a
    d = b
    nbiter4=0
    while (d-g) > 2*epsi and nbiter4<150:
    	nbiter4 = nbiter4+1
    	m = (d+g)/2
    	if ( f(g)*f(m)) <= 0 :
        	d=m
    	else : 
        	g = m
    
    return (d+g)/2 , nbiter4

def point_milieu(f,a,b,n):
	S = 0
	x1 = a
	w = (b-a)/n
	x2 = a + w
	import time as time
	start = time.clock()

	for i in range(n):
		c = (x1+x2)/2
		s = w*f(c)
		S = S + s
		x1 = x1 + w
		x2=x2 + w
	elapsed = (time.clock() - start )
	return S,elapsed

def enregistrer (methode, func, string, a, b, n):
	with open ('tableau_{:s}.txt'.format(string),'w') as fichier :
        	print('{0:12s} | {1:9s} | {2:s}'.format('    erreur', ' temps (sec)', 'n'))
 	        fichier.write('{0:15s}|{1:12s}|{2:s}\n'.format('    erreur', ' temps (sec)', 'n'))
	        for j in range(1, n+1):
			integrale,temps = methode(func, a, b, 10**j)
			erreur = abs(integrale -  I)
			print('{0:e} | {1:e} | {2:d}' .format(erreur, temps, 10**j))
			fichier.write('{0:9e} | {1:e} | {2:d}\n'. format(erreur, temps, 10**j))
	print('') 


def enregistrer_carlo(methode,string, n):
	with open ('tableau_{:s}.txt'.format(string),'w') as fichier :
        	print('{0:12s} | {1:9s} | {2:s}'.format('    erreur', ' temps (sec)', 'n'))
 	        fichier.write('{0:15s}|{1:12s}|{2:s}\n'.format('    erreur', ' temps (sec)', 'n'))
	        for j in range(1, n+1):
			erreur,temps = methode(10**j)
			print('{0:e} | {1:e} | {2:d}' .format(erreur, temps, 10**j))
			fichier.write('{0:9e} | {1:e} | {2:d}\n'. format(erreur, temps, 10**j))
	print('') 


def trapeze(f,a,b,n):
	S = 0
	w =(b-a)/n
	x1 = a
	x2 = a + w
	import time as time
	start = time.clock()
	
	for i in range(n):
        	s = ((f(x1)+f(x2))*w)/2
		S = S + s
		x1 = x2
		x2 = x2 + w
	elapsed = (time.clock() - start )
	return S, elapsed

def simpson(f,a,b,n):
	S=0
	w=(b-a)/n
	x1=a
	x2 = a+w
        import time as time
	start = time.clock()

	for i in range(n):
		s = w*(f(x1) + 4*f((x1+x2)/2) + f(x2))/6
		S = S+s
		x1=x2
		x2 = x2+w
        elapsed = (time.clock()-start)
        return S, elapsed
	


def Monte_Carlo(N):
	import math
	import numpy as np
	import time as time
	I = 0
	for i in range(N):
		X = 2*np.random.rand()-1
		Y = 2*np.random.rand()-1
	        if X > 1:
			X = cos(X)
		if Y > 1:
			Y = cos(Y)
	
		if ( X*X + Y*Y )< 1:	
			I = I + 1
	start = time.time()
	Er = abs(4*I/N - math.pi )
	r = time.time() - start
	return Er,r


def Monte_Carlo_boule(N):

	import math
	import numpy as np
	import time as time
	I = 0
	for i in range(N):
		X = 2*np.random.rand()-1
		Y = 2*np.random.rand()-1
		Z = 2*np.random.rand()-1
	        if X > 1:
			X = cos(X)
		if Y > 1:
			Y = cos(Y)
		if Z > 1:
			Z = cos(Z)
	
		if ( X*X + Y*Y + Z*Z )< 1:	
			I = I + 1
	start = time.time()
	Er = abs(8*I/N - math.pi*4/3 )
	r = time.time() - start
	return Er,r

def euler(f,u0,T,n):
 

  h = float (T)/n
  tt,uu = [],[]
  x0=0

  ui=u0
  xi=x0

  tt.append(x0)
  uu.append(u0)

  for i in range (x0,n):
	xi = xi + h
	ui = ui + h*f(xi,ui)
	tt.append(xi)
	uu.append(ui)
 
  return tt,uu 


