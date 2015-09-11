import numpy as np
from numpy.linalg import *

m = np.array(([ 8, 1, -2 , 3],
			  [-2, 5, 0.3, 1]
			 ,[ 1, 3,  10, 0]), dtype=float)

def GaussSeidel(m, iter = 100):
	if not 0 in m.diagonal():
		F = m.shape[0]
		C = m.shape[1]
		if not (F == C - 1):
			print 'Verifique los datos'
		mi = m[:,:-1]
		mr = m[:,-1].reshape(1,F)
		xsol = np.zeros((1,F))
		xsolant = np.full_like(xsol,None)
		c = 0
		while (c < iter) and (not np.allclose(xsol,xsolant)):
			c += 1
			print c
			xsolant = np.copy(xsol)
			for i in range(F):
				xfila = np.concatenate((mi[i, :i],mi[i, i+1:]))
				xvalor = np.concatenate((xsol[0, :i], xsol[0, i+1:]))
				xsol[0, i] = (mr[0, i] - sum(xfila * xvalor) / mi[i, i])
	return xsol

print GaussSeidel(m)




#vector = np.array(([1, 2, 3, 4]), dtype=float)
#print vector * 2, "\n"
#vector2 = vector[::-1]
#print vector * vector2