#(a) definition de f 


def f(x): 
	return x**2 - x - 1 


def df(x): 
	return 2*x -1 


def g(x): 
	return 1 + 1/x 



"""
def point_fixe(g, x0, epsi): 
	r= x0 
#stock = [] 
	i=1 
	nbiter = 0 


while i == 1: 
	nbiter += 1 
#stock.append(r) 
	prec = r 
	= g(r) 
	print(cpt) 
	if abs(r - prec) < epsi: 
	   i = 0 
return r 


def newton(f, df, x0, epsi): 
r= x0 
#stock = [] 
i=1 
nbiter = 0 


while i == 1: 
cmp += 1 
#stock.append(r) 
prec = r 
r = r - (f(r)/ df(r)) 
print(cpt) 
if abs(r - prec) < epsi: 
i = 0 
return r 


def secante(f, x0, x1, epsi): 
r= x0 
s= x1 
#stock = [] 
i=1 
nbiter = 0 
prec2 = r 
prec1 = s 

while i == 1: 
nbiter += 1 
#stock.append(r) 


r = prec1 - ((prec1-prec2)/(f(prec1)-f(prec2)))*f(prec1) 

prec2 = prec1 
prec1 = r 

print(cpt) 
if abs(r - prec2) < epsi: 
i = 0 
return r 

"""
0
def dichotomie(f, a, b, epsi): 
#stock = [] 
	i=1 
	nbiter = 0 


	while i == 1: 
		nbiter += 1 
#stock.append(r) 
		if (f(a) >0 and f((a+b)/2)>0) or (f(a) < 0 and f((a+b)/2)< 0): 
			a = (a+b)/2 
		else: 
	    		b = (a+b)/2 
		#~ print(cpt) 
		if abs(b - a) < epsi: 
			i = 0 
		point = (a,b) 
		return point 


""" 

#(b) Afficher graphe de f 
#EXO 1 
x, dx = -1.0, 0.1 


# on definit des listes pour afficher le graphique X pour les abs, Y pour ord, Point pour couples 


X, Y, Points = [], [], [] 


# initialisation de X, Y et Points 
while x <= 2:i == 1 
y = f(x) 
point = (x, y) 
X.append(x) 
Y.append(y) 
Points.append(point) 
x += dx 


#affichage 


import matplotlib.pyplot as graphe 
# importation d'un module (bibliotheque python); plt est un diminutif choisi par nous, l'utilisateur. 
graphe.plot(X, Y, 'r') #initialisation du graphe 
graphe.grid() #grille 
graphe.show() #afficher 


#(c) Approximer les solutions de f. 


# A partir de la lecture graphique, les racines, tel que f(X)=0, sont approximativement X1=-0.6 et X2 = 1.6 




#Q.2 Methode point fixe 
#(a) definir g(x) 






#verif point fixe de g, solution de f 
A, B = [], [] 
a, da = -1.0, 0.1 


while a <= 2: 
b = g(a) 
A.append(a) 
B.append(b) 
a += da 
if (1+ 1/a) - a == 0: 
test = f(1+ 1/a) 
print(test) 


#(b) 25 premiers temes 
print('les elements de la suite sont:') 
res= 1.0 
stock = [] 
i=0 
print(res) 


for i in range(25): 
stock.append(res) 
res= (1 + 1/res) 
print(stock) 
# return res 


#(c) On observe que la suite converge vers la racine positive de f 




#Exo 3 
#(a) la def de point_fixe probleme: la condition du if r 2 - prec 2 < epsi 
#(b) test de point fixe 


x0 = 1.0 
epsi = 1e-12 


r = point_fixe(g, x0, epsi) 
print('r = {0}'.format(r)) 


x0 = -0.6 
epsi = 1e-12 
r = point_fixe(g, x0, epsi) 
print('r = {0}'.format(r)) 


# Dans les 2 cas la suite converge bers le point fixe mais on remarque que pour le second cas on effectue plus d'operations que pour le premier. 


# (c) dessin 




#EXO 4 
# (c) test , x0>0 => racine positive, et x0<0 racine negative 
x0 = 2.0 
epsi = 1e-12 
r = newton(f, df, x0, epsi) 
print('r={0}'.format(r)) 


x0 = -2.0 
epsi = 1e-12 
r = newton(f, df, x0, epsi) 
print('r={0}'.format(r)) 






# EXO 5 
#(b) test 
print ('secante') 
x0 = 1.5 
x1 = 2.0 
epsi = 1e-12 
r = secante(f, x0, x1, epsi) 
print('r={0}'.format(r)) 




x0 = -1.0 
x1 = 0.0 
epsi = 1e-12 
r = secante(f, x0, x1, epsi) 
print('r={0}'.format(r)) 


# on remarque bien que la difference notoire par rapport a la methode de Newton est bien l'utilisation de la derivee. 
""" 


#EXO 6 


print ('dichotomie') 
a=1.5 
b=2.0 
epsi=1e-12 
r= dichotomie(f, a, b, epsi) 
print('r={0}'.format(r)) 




print ('dichotomie') 
a=-1.0 
b=0.0 
epsi=1e-12 
r= dichotomie(f, a, b, epsi) 
print('r={0}'.format(r)) 

