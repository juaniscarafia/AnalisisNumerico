import numpy as np
from numpy.linalg import *

m = np.array(([ 8, 1, -2 , 3],
			  [-2, 5, 0.3, 1]
			 ,[ 1, 3,  10, 0 ]), dtype=float)

F = m.shape[0]
C = m.shape[1]

if not ((F == C - 1) or (0 in m.diagonal())):
	print 'verifique los datos'
else:
	for i in range (F):
		m[i]= m[i]/m[i,i]
		for c in range(F):
			if not i == c:
				m[c]=m[c]-(m[i]*m[c,i])
	resultados = m[:,-1] #guarda la ultima columna en un vector

print m
print resultados