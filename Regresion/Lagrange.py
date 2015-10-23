import numpy as np
import Sistemas_Ecuaciones as gj

x = np.array([0,1,3,4,6], dtype = float)

y = np.array([3,5,21,35,75], dtype = float)

# m = np.array(([1,2,5], [4,3,10]), dtype=float)

def lagrange(x, y, valorinterp):
	n = x.shape[0] - 1
	soluc = 0
	for j in range(0, n+1):
		numerador = 1
		denominador = 1
		for i in range(0, n+1):
			if i != j:
				numerador = numerador * (valorinterp - x[i])
				denominador = denominador * (x[j] - x[i])
		soluc += y[j] * (numerador/denominador)	
	print soluc, "\n"

while True:
	try:
		valorinterp = int(raw_input("Ingrese el valor a interpolar (o una letra para salir):"))
	except ValueError:
		break
	lagrange(x,y, valorinterp)