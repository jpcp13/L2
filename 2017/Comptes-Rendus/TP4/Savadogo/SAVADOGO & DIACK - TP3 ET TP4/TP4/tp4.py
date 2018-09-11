from math import *
from methods import *
def premier(a):
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

#print premier(3001)
#print premier(49999)
#print premier(17)


print('\n')
print euclide(4864, 3458)




print bezout(4864, 3458)






