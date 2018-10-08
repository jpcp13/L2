from math import log, sqrt
def li(x):
	R = sqrt(x)
	g = 0.577215664901532
	p = -2.0
	S = g + log(log(x))
	for n in range(1, 16):
		p *= -0.5*log(x)/n
		I = 0
		for k in range((n-1)//2 + 1):
			I += 1/(2*k+1)
		#print("p = {}, I = {}".format(p, I))
		S += R*p*I
	return(S)
