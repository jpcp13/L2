import numpy as np

#exo 3

def euler(f, u0, T, n):
	h = T/n
	tt = np.zeros(n)
	uu = np.zeros(n)
	uu[0] = u0
	tt[0] = 0
	for i in range(1, n):
		u1 = u0 - h*u0
		uu[i] = u1
		tt[i] = h*i
		u0 = u1
	return uu, tt
#exo 5 
#c		

def euler2(F, U0, T, n):
	U = U0
	d = U0.shape[0]
	t = 0.0
	h = T/n
	tt = np.zeros(n)
	UU = np.zeros((d, n))
	for i in range (n):
		if(d ==1 ):
			UU = U
		else:
			UU[:, i] = U
		tt[i] = t
		U = U + h*F(t,U)
		t += h
	return tt, UU

