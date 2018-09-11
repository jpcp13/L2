""" 
module contennat  ...   
"""
import time
import random

def point_milieu(f,d,b,n):
    depart = time.clock()
    X, C, A = [], [], []
    
    for i in range(n):
        
            #On definit les subdivisions
            x=d + ((b-d)/(n-1))*i
            X.append(x)
            
    #On determine le milieu de chaque subdivision
    for i in range(n-1):
            c=(X[i]+X[i+1])/2
            C.append(c)
    
    #Calcul des aires f(c[i]) represente la hauteur
    for i in range(n-1):
            a=(f(C[i])*((b-d)/(n-1)))
            A.append(a)
    
    '''
    Calcul de l'aire totale sous la courbe en faisant
    la somme des aires des petits rectangles
    '''
    s = 0
    for i in range(n-1):
            s=A[i]+s
    arrivee = time.clock()
    return s, arrivee-depart


def trapeze(f,a,b,n):  
     depart = time.clock()
     h = (b - a)/n
     S = 0
     
     for i in range(n):
         xg = a + h*i
         xd = a + (i+1)*h
         s = h*((f(xd)+f(xg)))/2
         S = S + s
     arrivee = time.clock()
     
     return S, arrivee-depart

#Methode de simpson

def point_simpson (f,a,b,n):
	m = (b - a)/n
	xi = a
	xj = a
	i = 1
	S = 0
	while i <= n:
            	xi = a + m*i
		xj = a + m*(i - 1)
		si = (f(xi) + 4*f((xi + xj)/2) +f(xj))/6*m
		S = S + si
        	i = i + 1
	return S


#Methode de Monte_Carlo

def monte_carlo (N):
	L = 0
	M = 0
	XA, YA = [] ,[]
	XB, YB = [] ,[]
	for i in range(0,N):
		x = random.uniform(-1,1)
		y = random.uniform(-1,1)
		if(x**2 + y**2 <= 1):
			XA.append(x)
			YA.append(y)
			L = L + 1#point interieurs
		else:
			XB.append(x)
			YB.append(y)
			M = M + 1
	return 4.0*L/N
