

def euclide(a,b):
    
    d,u,v,d1,u1,v1=a,1,0,b,0,1  
    while d1!=0:
        q=d//d1
        d,u,v,d1,u1,v1=d1,u1,v1,d-q*d1,u-q*u1,v-q*v1
    return (d,u,v)

a,b = 4864, 3458

d,u,v= euclide(a,b)
print 'pgcd(%d,%d) = %d' % (a,b,d)
print '(%d)*%d + (%d)*%d = %d' %(u,a,v,b,d) 


