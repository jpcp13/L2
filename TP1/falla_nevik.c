#include < stdio,h >
/*J’ai crée plusieurs fonction répondre aux questions


/*1) a) fonction f

float f (float x)

{float x,y ;
 
 y=x*x-x-1 ;

return y ;

}

/* fonction g

float g (float x)

{ float x,y ;

y=1+1/x ;
return x ;
}
/fonction qui vérifie que les points fixes de g sont les 0 de f

void vérifgetf ( float a float b)

{float a,b , c,d;
 
printf(« chosissez vos points fixes »);

scanf(«%f %f »,&a ,&b);

c= g(a) ;
d=g(b) ;

if(a==c && b==d)
{c=f(a) ;
d=f(d) ;
if (c==0 && d==0)
 printf(« les points fixes de g sont bien les zéros de f bravos ») ;
}
else(
printf(« vous vous êtes trompé dans vos point fixe) ;
}

/*boucle pour calculer les 25 premier thermes de  2 .b
float a,b ;
int i ;
for(i==1 ;i<26;i++)
{
a=i ;
b=f(a) ;
printf(« pour a =% f(a)=%d »,i ,b) ;
}


 

