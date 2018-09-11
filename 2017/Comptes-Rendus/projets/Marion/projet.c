/* Declaration de fonctionnalites supplementaires */
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define NMAX 50

/* Declaration des fonctions utilisateurs */
int menu();
int menu2();
void affiche_tab(int T[], int n);
void trietab(int Tab[], int n);
int entier(int n);
void binaire(int n);

/*Fonction principale*/
int main()
{
	/* Declaration et initialisation des variables*/
	int Tab[NMAX];
	int Tabe[NMAX];
	int n, i;
	int choix=1;

	printf("Kahina et Marion vous souhaite la bienvenue dans leur programme de convertion de nombre entier en binaire.\n\n");
	
	while(choix!=0)
	{
		choix= menu(); /*Appel de la fonction menu*/
		switch(choix)
		{
			case 1 : /* Premier choix */
				printf("Entrez un nombre binaire (8 bits) :"); /* Recuperation des donnees */
				scanf("%d", &n);
				printf("\n");
				
				int e=entier(n);/* Appel de la fonction entier */
				printf("%d correspond à %d.\n", n, e);
				printf("\n");
				break;

			case 2 : /*Deuxieme choix */
				printf("Entrez un nombre entier (inférieur à 128) :"); /* Recuperation des donnees */
				scanf("%d",&n);
				printf("\n");
				
				while (n>=128) /* Erreur dans l'entree des donnees */
				{ 
					printf("Erreur, impossible de coder ce nombre, nous vous avons dit inférieur a 128 !\n Veuillez entrer un autre nombre :");
					scanf("%d",&n);
				}
				printf("\n");

				/* Appel de la fonction binaire */
				printf("%d correspond à ", n);
				binaire(n);
				printf("\n\n");
				break;
				
			case 3 : /* Troisieme choix */

				/* Recuperation des donnees */
				printf("Combien de valeurs binaire à trier ?\n");
				scanf("%d", &n);
				printf("\n");

				printf("Donner les valeurs binaire à trier :\n");
				for(i=0; i<n; i++)
				{
					scanf("%d", &Tab[i]);
				}
				
				printf("\n");
				printf("----valeurs binaires à trier----\n");
				affiche_tab(Tab, n); /* Appel de la fonction */
				printf("\n");

				for(i=0; i<n; i++)
				{
					Tabe[i] = entier(Tab[i]);
				}
				
				printf("\n");
				printf("----valeurs convertient en entiers à trier----\n");
				affiche_tab(Tabe, n); /* Appel de la fonction */
				printf("\n");
				
				printf("----en cours de tri----\n");
				trietab( Tabe, n);
				printf("\n");
				break;

			case 4 : /* Quatrieme choix */
				/* Recuperation des donnees */
				printf("Combien de valeurs à trier ?\n");
				scanf("%d", &n);
				printf("\n");

				printf("Donner les valeurs à trier :\n");
				for(i=0; i<n; i++)
				{
					scanf("%d", &Tabe[i]);
				}
				
				printf("\n");
				printf("----valeurs à trier----\n");
				affiche_tab(Tabe, n); /* Appel de la fonction */
				printf("\n");

				printf("\n");
				printf("----valeurs à trier en binaire----\n");
				for(i=0; i<n; i++)
				{
					binaire(Tabe[i]);
					printf("\t");
				}
				printf("\n\n");
				
				printf("----en cours de tri----\n");
				trietab( Tabe, n);/* Appel de la fonction */
				printf("\n");
				break;

			default : /* Quitter */
				printf("Nous vous souhaitons une bonne fin de journee, au revoir !\n");
				printf("\n");
		}
		if(choix!=0)
		{		
			choix=menu2(); /* Appel de la fonction menu2 */

				if(choix==0) /* Quitter */
				{
					printf("Nous vous souhaitons une bonne fin de journee, au revoir !\n");
				printf("\n");	
				}
		}
	}
	
	/* valeur fonction */
	return EXIT_SUCCESS;

}

/* Fonction menu */
int menu ()
{
	/* Declaration et initialisation des variables */	
	int m;

	printf("Faites le choix de votre convertion\n \n");
	printf("1 : D'un nombre binaire en entier\n");
	printf("2 : D'un entier en nombre binaire\n");
	printf("3 : Tableau de nombres binaire en entiers\n");
	printf("4 : Tableau d'entiers en nombres binaire\n");
	printf("0 : Quitter\n \n");
	printf("Tapez votre choix : ");
	scanf("%d", &m);
	printf("\n");
	
	/* valeur fonction */
	return m;
}

/*Fonction menu2 */
int menu2()
{
	int m;

	printf("Continuer ? \n Taper 1 pour continuer ou 0 pour quitter : ");
	scanf("%d", &m);
	printf("\n");

	/* valeur fonction */
	return m;
}

/* Fonction convertion de binaire en entier */
int entier(int n)
{
	if (n<10)
		return n;
	else
		return 2*entier(n/10)+n%2;

}

/* Fonction convertion d'entier en binaire */
void binaire(int n)
{
	/* Declaration des variables*/
	int t[8], i = 0, k=0;

	do{
		t[i] = n%2;
		n = n/2;
		i++;
		k++;
	}while(n != 0);
     
	for(i = k-1; i >= 0; i--)
		printf("%d", t[i]);
}

/* Fonction affiche tableau */
void affiche_tab(int T[], int n)
{
	/* Declaration des variables */
	int i;

	for( i=0; i<n; i++)
	{
		printf("%d\t", T[i]);
	}
	printf("\n");
}

/* Fonction trier tableau */
void trietab( int Tab[], int n)
{
	/* Declaration des variables */
	int i, j, aux;

	i=-1;
	
	while(i<n-1)
	{
		for( j=n-2; j>i; j--)
		{
			if( Tab[j]>Tab[j+1] )
			{
				aux=Tab[j];
				Tab[j]=Tab[j+1];
				Tab[j+1]=aux;
				affiche_tab(Tab, n);
			}
		}
		i++;
	}
	printf("\n\n");
	printf("----valeurs binaires triées----\n"); /* Convertion en binaire */
	for(i=0; i<n; i++)
	{
		binaire(Tab[i]);
		printf("\t");
	}
	printf("\n\n");
}


