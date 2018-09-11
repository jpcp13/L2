

#Resolution numerique de Ax = B 

import numpy as np 

A = np.array([[2, 4, 4, 1],
	[3, 6, 1, 2],
	[1, 1, 2, 3],
	[1, 1, 4, 1]])
B = np.array([1,4,8,7])

def recherche_pivot(A, b, j):
  p = j
  for i in range(j+1, A.shape[0]):
    if abs(A[i, j]) > abs(A[p, j]):
      p = i
  if p != j:
    b[[p, j]] = b[[j, p]]
    A[[p, j]] = A[[j, p]]

def elimination_bas(A, b, j):
  for i in range(j+1, A.shape[0]):
    b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]
    A[i] = A[i] - (A[i, j] / A[j, j]) * A[j]

def descente(A, b):
  for j in range(A.shape[1] - 1):
    recherche_pivot(A, b, j)
    elimination_bas(A, b, j)

def elimination_haut(A, b, j):
  for i in range(j):
    b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]

def remontee(A, b):
  for j in range(A.shape[1] - 1, 0, -1):
    elimination_haut(A, b, j)

def solve_diagonal(A, b):
  for k in range(b.shape[0]):
    b[k] = b[k] / A[k, k]
  return b

def gauss(A, b):
  U = A.copy()
  v = b.copy()
  descente(U, v)
  remontee(U, v)
  return solve_diagonal(U, v)

c = gauss(A,B)
print(c)

def determinant(A):
	U = A.copy()
	d = 1
	for j in range(U.shape[1] - 1):
		# recherche du pivot
		p = j
		for i in range(j+1, U.shape[0]):
			if U[i, j] > U[p, j]:
				p = i
		# permutation des deux lignes
		if p != j:
			d *= -1
			U[[p, j]] = U[[j, p]]
		# élimination
		for i in range(j+1, U.shape[0]):
			U[i] = U[i] - (U[i, j] / U[j, j]) * U[j]
	# produit des éléments diagonaux
	for k in range(U.shape[0]):
		d *= U[k, k]
	return d
