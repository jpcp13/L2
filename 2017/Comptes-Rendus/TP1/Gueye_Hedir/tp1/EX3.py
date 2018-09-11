

# On a une erreur au niveau de la ligne 11 que l'on a pas su resoudre

#Partie 3: point fixe

def point_fixe(g,x0,epsi):
	x=x0
	d=2*epsi
	compt=0
     nbiter=0
	while d>epsi:
          compt +=1
		x1=g(x)
		d=abs(x1-x)
          print('x. = {0}, compteur ={1}\n').format(x,compt)
          x=x1
     print('Le nombre diteration est ={0}').format(compt)
	return x, nbiter

#3.b)

#Test 1
n= "Test 1 de point fixe"
print(n)
print("\n")
x0=1.0
epsi=10**-12
def g(x):

	return 1+ 1/x


r, nbiter=point_fixe(g,x0,epsi)
print("\n")

#Test 2
n="Test 2 point fixe"
print(n)
print("\n")
x0=-0.6
epsi=10**-12