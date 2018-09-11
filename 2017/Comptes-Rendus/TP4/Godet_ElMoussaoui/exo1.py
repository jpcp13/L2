#test a)

a = 3
b = 2
c = float(a/b)

print c
print float(a/b)
print float(a//b)
print (a%b)
print "\n"

#Definition de fonctions

def is_prim(n):
	for i in range(2,n-1):
		if(n % i == 0):
			return False
		 
	return True
		

def show_prim(n):
	if (is_prim(n) != False):
		print n,"est premier"
	else:
		print n,"n'est pas premier"

def Fermat(n):
	return 2**(2**n) + 1

#Nombre premier

show_prim(3)
show_prim(10)
show_prim(1001)
show_prim(2017)
show_prim(3001)
show_prim(49999)
show_prim(89999)

for j in range(6):
	print "\n"
	print "Fermat(",j,") = ",Fermat(j)
	show_prim(Fermat(j))
	

