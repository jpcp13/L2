#Idoufker Aboubakr
import random
from module import *
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
a = 1.0
b = -6.0
c = 11.0
d = -6.0
epsi = 10**-15
def f3(a,b,c,d,X):
	return a*X**3 + b*X**2 + c*X + d

def df3(a,b,c,d,X):
	return 3*a*X**2 + 2*b*X + c 

t = np.linspace(-20.0, 20.0, 100)
plt.clf()
plt.plot(t, f3(a,b,c,d,t),'k-', t, df3(a,b,c,d,t) ,'r-')
plt.axis([-10, 10, -15, 15])
plt.grid('on')
plt.savefig('Graphique.png')

def tvi(a, b, c, d, f3, epsi):
	D = 4.0*(b**2) - 12.0*a*c
	u = 1.0
	v = 0.0
	u1 = 1.0
	u2 = 1.0
	u3 = 1.0
	v1 = 0.0
	v2 = 0.0
	v3 = 0.0
	if (D > 0.0) :
		x1 = (-2.0*b - sqrt(D))/(6*a)
		x2 = (-2.0*b + sqrt(D))/(6*a)
		if (f3(a,b,c,d,x1)*f3(a,b,c,d,x2) > 0.0):
			while (f3(a,b,c,d,u)*f3(a,b,c,d,v) > 0.0):
				u = 1.0/random.uniform(-1.0,1.0)
				v = 1.0/random.uniform(-1.0,1.0)
			m = (u + v)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u)*f3(a,b,c,d,m) > 0.0):
					u = m
				if(f3(a,b,c,d,v)*f3(a,b,c,d,m) > 0.0):
					v = m
				m = (u + v)/2.0
				delta = abs(v - m)
			return m
		if (f3(a,b,c,d,x1) == 0):
			while (u >= v or (f3(a,b,c,d,u)*f3(a,b,c,d,v) > 0.0) or a*u < a*x1 or a*v < a*x1):
				u = 1.0/random.uniform(-1.0,1.0)
				v = 1.0/random.uniform(-1.0,1.0)
			m = (u + v)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u)*f3(a,b,c,d,m) > 0.0):
					u = m
				if(f3(a,b,c,d,v)*f3(a,b,c,d,m) > 0.0):
					v = m
				m = (u + v)/2.0
				delta = abs(v - m)
			return m,x1
		if (f3(a,b,c,d,x2) == 0):
			while (u >= v or (f3(a,b,c,d,u)*f3(a,b,c,d,v) > 0.0) or a*u > a*x2 or a*v > a*x2):
				u = 1.0/random.uniform(-1.0,1.0)
				v = 1.0/random.uniform(-1.0,1.0)
			m = (u + v)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u)*f3(a,b,c,d,m) > 0.0):
					u = m
				if(f3(a,b,c,d,v)*f3(a,b,c,d,m) > 0.0):
					v = m
				m = (u + v)/2.0
				delta = abs(v - m)
			return m,x2
		else :
			while (u1 >= v1 or (f3(a,b,c,d,u1)*f3(a,b,c,d,v1) > 0.0) or a*u1 > a*x1 or a*v1 > a*x1):
				u1 = 1.0/random.uniform(-1.0,1.0)
				v1 = 1.0/random.uniform(-1.0,1.0)
			m1 = (u1 + v1)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u1)*f3(a,b,c,d,m1) > 0.0):
					u1 = m1
				if(f3(a,b,c,d,v1)*f3(a,b,c,d,m1) > 0.0):
					v1 = m1
				m1 = (u1 + v1)/2.0
				delta = abs(v1 - m1)
			while (u3 >= v3 or (f3(a,b,c,d,u3)*f3(a,b,c,d,v3)) > 0.0):
				u3 = random.uniform(x1,x2)
				v3 = random.uniform(x1,x2)
			m3 = (u3 + v3)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u3)*f3(a,b,c,d,m3) > 0.0):
					u3 = m3
				if(f3(a,b,c,d,v3)*f3(a,b,c,d,m3) > 0.0):
					v3 = m3
				m3 = (u3 + v3)/2.0
				delta = abs(v3 - m3)
			while (u2 >= v2 or (f3(a,b,c,d,u2)*f3(a,b,c,d,v2) > 0.0) or a*u2 < a*x2 or a*v2 < a*x2):
				u2 = 1.0/random.uniform(-1.0,1.0)
				v2 = 1.0/random.uniform(-1.0,1.0)
			m2 = (u2 + v2)/2.0
			delta = 2*epsi
			while delta > epsi:
				if(f3(a,b,c,d,u2)*f3(a,b,c,d,m2) > 0.0):
					u2 = m2
				if(f3(a,b,c,d,v2)*f3(a,b,c,d,m2) > 0.0):
					v2 = m2
				m2 = (u2 + v2)/2.0
				delta = abs(v2 - m2)
		return m1, m2, m3
	else :
		x0 = (-2.0*b)/(6*a)
		if (f3(a,b,c,d,x0) == 0.0) :
			return x0
		while u >= v or (f3(a,b,c,d,u)*f3(a,b,c,d,v) > 0.0):
			u = 1.0/random.uniform(-1.0,1.0)
			v = 1.0/random.uniform(-1.0,1.0)
		m = (u + v)/2.0
		delta = 2*epsi
		while delta > epsi:
			if(f3(a,b,c,d,u)*f3(a,b,c,d,m) > 0.0):
				u = m
			if(f3(a,b,c,d,v)*f3(a,b,c,d,m) > 0.0):
				v = m
			m = (u + v)/2.0
			delta = abs(v - m)
		return m
def cardan(a,b,c,d):
	p = (-(b**2) + 3.0*a*c)/(3.0*a**2)
	q = (2.0*(b**3) - 9.0*a*b*c + 27.0*(a**2)*d)/(27.0*(a**3))
	D = -4.0*(p**3) - 27.0*(q**2)
	j = -1.0/2.0 + (sqrt(3)/2.0)*1j
	jc = np.conj(j)	
	if (abs(D) < 1e-16):
		D = 0.0
	if D < 0.0 :
		u = sqrtreel3((-q + sqrt(abs(D/27.0)))/2.0)
		v = sqrtreel3((-q - sqrt(abs(D/27.0)))/2.0)
		z1 = u + v - b/(3.0*a)
		z2 = j*u + jc*v - b/(3.0*a)
		z3 = jc*u + j*v - b/(3.0*a)
		return z1,z2,z3
	if D == 0.0 :
		z0 = 3.0*q/p - b/(3.0*a)
		z1 = -3.0*q/(2.0*p) - b/(3.0*a)
		return z1,z0
	if D > 0.0 :
		u = sqrtcmpx3((-q + 1j*sqrt(D/27.0))/2.0)[0]
		z1 = u + np.conj(u) - b/(3.0*a)
		z2 = j*u + np.conj(j*u) - b/(3.0*a)
		z3 = jc*u + np.conj(jc*u) - b/(3.0*a)
		return z1,z2,z3

def tschirnhaus (a,b,c,d,f3,eq2):	
	p = (-(b**2) + 3.0*a*c)/(3.0*a**2)
	q = (2.0*(b**3) - 9.0*a*b*c + 27.0*(a**2)*d)/(27.0*(a**3))
	D = 81.0*(q**2) + 12.0*(p**3)
	if (abs(D) < 1e-16):
		D = 0.0
	if (D < 0.0) :
		at = 9.0*q + 1j*sqrt(-D)
		bt = 2.0*(p**2)
		ct = 2.0*at*p/3.0
	if (D == 0.0) :
		at = 9.0*q
		bt = 2.0*(p**2)
		ct = 6.0*q*p
	if (D > 0.0):
		at = 9.0*q - sqrt(D)
		bt = 2.0*(p**2)
		ct = 2.0*at*p/3.0
	yt = 3.0*at*bt*ct*q + (q**2)*(at**3) -q*(bt**3) + (p**2)*(at**2)*ct + 2.0*(bt**2)*ct*p - p*q*(at**2)*bt-2.0*at*(ct**2)*p+(ct**3)
	y1,y2,y3 = sqrtcmpx3(yt)
	S = [0j, 1.0j, 2.0, 3.0, 4.0, 5.0]
	S[0],S[1] = eq2(at,bt,(ct-y1))
	S[2],S[3] = eq2(at,bt,(ct-y2))
	S[4],S[5] = eq2(at,bt,(ct-y3))
	T = []
	for i in range(0,6):
		t = S[i] + b/(3.0*a)
		f = f3(a,b,c,d,t)
		if abs(f) < 1e-10 :
			T.append(t)
	return T



