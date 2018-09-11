from prime import*
from bezout import*

p=rdm_prime(2**35, 2**36) 
q=rdm_prime(2**35, 2**36)
print("q=",q,"p",p)

n=p*q
print("n=",n)
print(n>(2**70))

phi=(p-1)*(q-1)
print("phi=",phi)

e=random.randint(2,phi)
d=pgcd(phi,e)
while(d!=1):
	e=random.randint(2,phi)
	d=pgcd(e,phi)
	
print("e=",e)

d,u,v =euclide(e,phi)
print("u:",u)
u = u%phi
print("u=",u)

M=911951247083361712609
print("M=",M)
C=pow(M,e,n)
print("C=",C)

N=pow(C,u,n)
print("dechiffrement M=",N)

####### rsa_key
def rsa_key():
	q=rdm_prime(2**35,2**36)
	p=rdm_prime(2**35,2**36)
	n=q*p
	phi=(p-1)*(q-1)
	e=random.randint(2,phi)
	d=pgcd(phi,e)
	while(d!=1):
		e=random.randint(2,phi)
		d=pgcd(e,phi)
	u = euclide(e,phi)[1] % phi
	return e, u, n
print(rsa_key())
###############

def word2int(w):
	nbr = '' # ecriture binaire de l'entier nbr
	cplmt = 10 - len(w)
	while cplmt>0:
		w = w + '\0'
		cplmt = cplmt - 1
	for i in range(len(w)):
		bin_c = '{:b}'.format(ord(w[i]))
		# bin_c: string contenant l'ecriture binaire du code ascii de la i-eme lettre du mot w
		cplmt2 = 7 - len(bin_c) # complete avec des 0 devant bin_c si plus petit que 7
		while cplmt2>0:
			nbr = nbr + '0'
			cplmt2 = cplmt2 - 1
		for k in range(len(bin_c)):
			nbr = nbr + bin_c[k]
	return int(nbr, 2) # convertir nbr de base2 en base10 et le retourner
	
def int2word(n): 
	n_bin = '{:b}'.format(n) # n de base10 en base2
	while len(n_bin)<70:
		n_bin = '0' + n_bin # complementer le nombre binaire avec des 0 devant si besoin
	mot = ''
	for i in range(10):
		c = (n_bin[7*i] + n_bin[7*i+1] + n_bin[7*i+2] + n_bin[7*i+3] + 
		     n_bin[7*i+4] + n_bin[7*i+5] + n_bin[7*i+6]) # packet de 7bits
		mot = mot + chr(int(c,2))
	if mot[len(mot)-1]=='\0':
		tmp = ''
		c = 0
		while mot[c] !='\0':
			tmp = tmp + mot[c]
			c = c+1
		mot = tmp
	return mot
	
def chiffrer(texte, cle_public):
	#print(cle_public)
        with open(texte, 'r+') as f:
                texte_data = f.read()
        if texte_data[len(texte_data)-1]!='\n':
                texte_data = texte_data + '\n'#print('contenue:',texte_data)
        #print('longueur:',len(texte_data))
        with open('texte_chiffrer', 'w') as f:
                continuer = True
                k = 0
                mot = ''
                while continuer:
                        print(k)
                        if texte_data[k]!='\n' or (k+1)!=len(texte_data):
                                mot = mot + texte_data[k]
				#print mot
				#print("Condition",len(mot)==10 or (len(mot)==(len(texte_data)%10)-1 and len(texte_data)==k+2))
                                if len(mot)==10 or (len(mot)==len(texte_data)%10-1 and len(texte_data)==k+2):
                                        print(word2int(mot))
                                        nbr_coder = pow(word2int(mot), cle_public[0], cle_public[1])
                                        f.write(str(nbr_coder)+' ')
                                        mot = ''
                        else:
                                continuer = False
                        k = k + 1
			
def dechiffrer(texte, cle_prive):
	with open(texte, 'r+') as f:
		texte_data = f.read()
	print('contenue:',texte_data)
	print('longueur:',len(texte_data))
	with open('texte_dechiffrer.txt', 'w') as f:
		continuer = True
		k = 0
		nbr_coder = ''
		while continuer:
			print(k)
			if len(texte_data)>k:
				if texte_data[k]!=' ':
					nbr_coder = nbr_coder + texte_data[k]
					print('code:',nbr_coder)
				else:
					nbr = pow(int(nbr_coder), cle_prive[0], cle_prive[1])
					print(nbr)
					print(int2word(nbr))
					mot = int2word(nbr)
					f.write(mot)
					nbr_coder = ''
			else:
				if len(texte_data)==k:
					continuer = False
			k = k + 1
