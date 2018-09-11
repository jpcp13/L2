def is_primes(a):
    #Fonction booleenne qui dit si un nombre est premier ou non
    r=int(a**(0.5))+1
    resultat=True
    i=1
    
    if a==1:
        resultat=False
        #un nombre premier est un nombre qui admet exactement deux
        #diviseurs, 1 n'est pas premier
    elif a%2==0 and a<>2:
        resultat=False
        #Si 2 ne divise pas a alors aucun nombre pair ne divisera a

    
    while 2*i+1 <r+1 and resultat==True :
        #Si un nombre a n'est pas premier alors:
        #il existe un diviseur de a dans [2,racine(a)]
        
        if a%(2*i+1)==0:
            #On ne teste que pour les impairs cf plus haut
            resultat=False
            
        i=i+1
    return(resultat)


def primes(n, p=[2,3,5]):  #crible d'Eratosthene
    
    k = p[-1]+2
    if n < k:
        return [x for x in p if x<=n]
    while k <= n:
        i = 0
        while i < len(p):
            if p[i]*p[i] > k:
                p.append(k)
                break
            if (k % p[i]) == 0:
                break
            i += 1
        k += 2
    return p
 


def facteur(n):   #fonction qui decomopose le nombre en produits de facteurs premiers
	P = []
	i = 2
	while (n != 1): 
		if n % i == 0 and is_primes(i) == True:
			n = n/i
			P.append(i)
			i= i-1
		i = i+1
	print P




def euclide(a, b):     #fonction qui donne le pgcd et les coefficients de bezout
    r, u, v = a, 1, 0
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
    return ('pgcd = {0} ; u = {1} et v = {2}'.format(r,u,v))





