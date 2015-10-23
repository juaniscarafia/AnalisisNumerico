import numpy as np
import Sistemas_Ecuaciones as gj

x = np.array([0,1,3,4,6], dtype = float)

y = np.array([3,5,21,35,75], dtype = float)

# m = np.array(([1,2,5], [4,3,10]), dtype=float)

class Solucion:
    def __init__(self, valores, cc):
        self.valores = valores
        self.cc = cc

    def imprimir(self):
    	if self.valores is None:
    		print "Error: se produjo una division por cero al calcular el coeficiente de correlacion."
    	else:
	        print """================\n=== SOLUCION ===\n================"""
	        for i in range(len(self.valores)):
	            print "a" + str(i) + ": %f \n" % (self.valores[i])
	        print "Coeficiente de Correlacion: ", self.cc

def polinomial(x, y):


	sx = sum(x)
	sy = sum(y)
	n = x.shape[0]
	promx = sx / n
	promy = sy / n
	sxy = sum(x * y)
	sx2 = sum(x ** 2)

	grado = 0
	while (grado < 1):
		try:
			grado = int(raw_input("Ingrese el grado de la funcion:"))
		except ValueError:
			print "El valor ingresado no es valido. Intente nuevamente."
	m = np.zeros((grado + 1,grado + 2))
	#print m
	sx = sum(x)
	sy = sum(y)
	for i in range(n):
		for j in range(0, grado+1):
			for k in range(0, grado+1):
				m[j,k] = m[j,k] + x[i] ** (k+j)
			m[j, grado + 1] = m[j, grado + 1] + (y[i] * (x[i] ** j))
	#print m
	r = gj.Solucion()
	r = gj.GaussJordan(m)
	r = r.incognita

	st = 0
	sr = 0
	for i in range(n):
		st = st + ((promy - y[i]) ** 2)
		s = 0
		for j in range(0, grado+1):
			s = s + (r[j] * (x[i] ** j))
		sr = sr + ((s - y[i]) ** 2)
	if st != 0:
		corr = (np.sqrt(abs((st - sr) / st))) * 100
		soluc = Solucion(r, corr)
		return soluc
		#dar la Solucion
	else:
		soluc = Solucion(None, None)
		return soluc
		#salta error por div 0

polinomial(x,y).imprimir()