from numpy import *

def point_milieu(f ,a ,b , n):
	m = (b - a)/n
	xi = a
	xj = a
	i = 1
	S = 0
	ci =0
	while i <= n:
		xi = a + m*i
		xj = a + m*(i - 1)
		ci = (xi + xj)/2
		si  = m*f(ci)
		S = S + si
		i = i + 1
	return S

def point_trapeze (f ,a, b, n):
	m = (b - a)/n
	xi = a
	xj = a
	i = 1
	S = 0
	while i <= n:
		xi = a + m*i
		xj = a + m*(i - 1)
		si  = m*(f(xj) + f(xi))/2
		S = S + si
		i = i + 1
	return S

def point_simpson (f , a, b, n):
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
			L = L + 1
		else:
			XB.append(x)
			YB.append(y)
			M = M + 1
	return 4.0*L/N

