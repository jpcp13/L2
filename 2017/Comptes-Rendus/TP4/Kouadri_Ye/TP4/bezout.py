from factorisation import *

def pgcd(a,b):
        while(a%b!=0):
                tmp=a
                a=b
                b=tmp%b
        return b
##print(pgcd(10, 5))

a=132
b=72

def pgcdfactprems(a,b):
        l=factor(a)
        l2=factor(b)
        d=1
        g=[]
        f=[]
        s=0
        string = ''
        if a==0:
                return b
        elif  b==0:
                return a
        if a==1:
                return a
        elif  b==1:
                return b
                
        for i in range(len(l)):
                 if(not(l[i] in f)):
                        for j in range(len(l2)):
                                if(l[i]==l2[j]):
                                        f.append(l[i])
                                        k=0
                                        h=0
                                        for t in range(len(l)):
                                                if l[t]==l[i]:
                                                        k=k+1 #puissance du facteur premier dans l
                                        
                                        for m in range(len(l2)):
                                                if l2[m]==l[i]:
                                                        h=h+1 #puissance du facteur premier dans l2
                                        g.append(l[i])
                                        if(h>k):
                                                g.append(k)
                                        else: 
                                                g.append(h)
                                        break
                                else:
                                        s=s+1
                                if(s==len(l2)-1):
                                        f.append(l[i])
        for i in range(len(g)//2):
                d = d * g[2*i]**g[2*i+1]
                string = string + '{:d}^{:d}'.format(g[2*i], g[2*i+1])
                if i<len(g)//2-1:
                        string = string + ' x '
        return g, string, d

"""
print(pgcd(105,280))
print(pgcd(24,36))
print (pgcd(0,10))
print (factor(1))
print (factor(10))
print (pgcdfactprems(1,10))
print (pgcdfactprems(0,10))
print(pgcd(1,10))
"""

##print (pgcdfactprems(0, 10))
print(factor(4864))
print(factor(3458))
print(pgcd(4864, 3458))
print (pgcdfactprems(4864, 3458))

"""
print (pgcdfactprems(95, 57))
print (pgcdfactprems(24, 36))
print (pgcdfactprems(105, 280))
"""

def euclide(a, b):
        r1= a; u1 = 1; u2 = 0
        r2= b; v1= 0; v2= 1
        
        while r2!=0:
                q = r1//r2
                r3=r1; u3=u1; v3=v1
                r1=r2; u1=u2; v1=v2
        
                r2=r3 - q*r2
                u2=u3- q*u2
                v2=v3- q*v2
        return (r1, u1, v1)
print(euclide(4864,3458))
