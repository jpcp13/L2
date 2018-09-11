from math import *


def is_prime(n):
    if n%2==0:
        return False
    else:
        if n==0 or n==1:
            return False
        else:
            i=3
            while i<=sqrt(n):
                if n%i==0:
                    return False
                else:
                    i=i+1
            return True


L=is_prime(89999)#mettre le nombre dont on cherche s'il est premier ou pas
print L



    
