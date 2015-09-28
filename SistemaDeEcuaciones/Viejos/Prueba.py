import numpy as np
from numpy.linalg import *

m = np.array(([ 8, 1, -2 , 3],
			  [-2, 5, 0.3, 1]
			 ,[ 1, 3,  10, 0]), dtype=float)
		
F = m.shape[0]
C = m.shape[1]
mi = m[:,:-1]
mr = m[:,-1]
xsol = np.zeros((1,F))
xsolant = np.full_like(xsol,None)
c = 0
xfila = []
for i in range(F):
	xfila = np.concatenate((mi[i, :i],mi[i, i+1:]))
	print xfila
xvalor = np.concatenate((xsol[0, :i], xsol[0, i+1:]))
print xvalor
