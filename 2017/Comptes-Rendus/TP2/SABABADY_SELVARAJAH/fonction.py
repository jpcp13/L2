# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 
#*********************************************************

import numpy as np

def point_milieu(f,a,b,n):
        x0= a
        xx=[x0]
        for i in range(n) :
                 x1=x0+(b-a)/n
                 xx.append(x1)
                 x0=x1
        cc=[]
        for i in range (n):
                c=(xx[i]+xx[i+1])/2
                cc.append(c)
        ss=[]
        for i in range(n):
            s = ((b-a)/n)*f(cc[i])
            ss.append(s)
        S=0
        for i in range (n):
            S+=ss[i]

        return S

def trapeze(f,a,b,n) :
	h=(b-a)/float(n)
	t=0.5*(f(a)+f(b))
	for i in range(1,n) :
		t=t+f(a+i*h)
	return h*t

def Simpson(f,a,b,n) :
	h=(b-a)/float(n)
	s=(f(a)+f(b))/6
	for i in range(1,n) :
		s=s+f(a+i*h)/3
	for i in range(n) :
		s=s+f(a+(2*i+1)*h/2)*2/3
	return h*s


def monte_carlo(N):
	X = np.random.uniform(-1,1,N)
	Y = np.random.uniform(-1,1,N)
	I=0
	for i in range(N):
		if (X[i]**2+Y[i]**2)<=1:
			I+=1
	m=((I*4.0)/N)
	
	return m

def monte_carlo_2(N):	
	X = np.random.uniform(-1,1,N)
	Y = np.random.uniform(-1,1,N)
	Z = np.random.uniform(-1,1,N)
	I=0
	for i in range(N):
		if (X[i]**2+Y[i]**2+Z[i]**2)<=1:
			I+=1
	m=((6.0*I)/N)
	return m


