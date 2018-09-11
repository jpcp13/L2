#6) METHODE DE MONTE CARLO
#6-a) Tracé du cercle

theta = np.linspace(0, 2*np.pi, 100)
Xcercle = np.cos(theta)
Ycercle = np.sin(theta)
plt.plot(Xcercle, Ycercle)
plt.axis("equal")
#plt.show()
plt.savefig('cercle.png')


#6-b) Valeurs aleatoires en 0 et 1
print('\n')
import numpy.random as npr
print('Quelquesvaleurs aleatoires entre 0 et 1:')
print (npr.rand(10))

#Valeurs aleatoires en -1 et 1
print('\n')
print('Quelques valeurs aleatoires entre -1 et 1:')
print(npr.uniform(-1, 1, 10))


for i in range(100):
	xpoint = 2*np.random.rand()-1
	ypoint = 2*np.random.rand()-1
	if (xpoint**2+ypoint**2)<1:
		plt.scatter(xpoint, ypoint, color='red', marker='.')
	else:
		plt.scatter(xpoint, ypoint, color='green', marker='.')

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)
plt.savefig('cercle2.png')



