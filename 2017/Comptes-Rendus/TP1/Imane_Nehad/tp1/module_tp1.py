def f(x):
	return x**2 - x - 1.0

def df(x):
	return 2*x - 1.0

def g(x):
	return 1 + 1/x

def point_fixe(g, x0, epsi):
	x=x0
	delta = 2*epsi
	cpt = 0
	while delta > epsi:
		x1=g(x)
		delta = abs(x1-x)
		x=x1
		cpt+= 1
	return x, cpt

def newton(f, df, x0, epsi):
	x = x0
	delta = 2*epsi
	cpt = 0
	while delta > epsi:
		x1 = x - f(x)/df(x) # x est la valeur courante (equivalent a x_n), x1 est la valeur suivante (equivalent a x_n+1)
		delta = abs(x1-x)
		x = x1
		cpt+= 1
	return x , cpt

def secante(f, x0, x1, epsi):
	delta = 2*epsi
	c=0
	cpt= 0
	while delta > epsi and c < 100:
		# x0 va representer x_{n-1}, x1 va representer x_n, x2 va representer x_{n+1} dans la recurrence donnee par l'enonce.
		
		y0, y1 = f(x0), f(x1)
		
		#print('denominator =', y1 - y0)
		#nous avons fait ce test pour savoir a partir de quel moment le denominateur est considere comme nul
		
		x2 = x1 - (x1-x0)/(y1 - y0) * f(x1)
		delta = abs(x2-x1)
		# je mests a jour x0, x1
		x0, x1 = x1, x2 # syntaxe python; en C, on aurait ecrit deux lignes.
		c+=1
		cpt+= 1 
	return x2 , cpt

def dichotomie(f, x0, x1, epsi):
	delta= 2*epsi
	c=0
	cpt= 0
	#on rajoute un compteur pour eviter d'avoir une boucle a l'infinie
	while delta > epsi and c < 100 :
		if (f(x0) >0 and f((x0+x1)/2)>0) or (f(x0) < 0 and f((x0+x1)/2)< 0):
			x0 = (x0+x1)/2
		else: 
			x1 = (x0+x1)/2
			delta = abs(x1-x0)
			
		c+= 1
		cpt += 1
	return x1 , cpt
