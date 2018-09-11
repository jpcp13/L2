# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

def point_fixe(g,x0,epsi):
	x=x0
	d=2*epsi
	compt=0
	while d>epsi:
		x1=g(x)
		d=abs(x1-x)
		x=x1
		print (x)
	return x


def newton(f,df,x0,epsi):
	d=2*epsi
	x=x0
	compt=0
	while d > epsi and compt < 40:
		compt += 1
		v=x-f(x)/df(x)
		x=v
		print('x = {0}, compteur = {1}\n'.format(x,compt))
	return v
    

def secante(f,x0,x1,epsi):
	delta=2*epsi
	cpt=0
	while delta > epsi and cpt < 100:
		cpt+=1
		num = x1-x0
		delta = abs(num)
		den = f(x1)-f(x0)
		x2=x1-num/den*f(x1)
		x0=x1
		x1=x2
		print('x = {0},compteur = {1}\n'.format(x2,cpt))
	return x2
    

def dichotomie(f, a, b, epsi,cpt):
    if b-a<=epsi:
        print(a,b,cpt)
        return a,b,cpt
    else:
	cpt+=1
        c=(a+b)/2
        if f(a)*f(c)<=0:
            return dichotomie(f,a,c,epsi,cpt)
        else:
            return dichotomie(f,c,b,epsi,cpt)

