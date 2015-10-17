





























import numpy as np
import Sistemas_Ecuaciones as gj

x = np.array([0,1,3,4,6], dtype = float)

y = np.array([2,4,12,19,39], dtype = float)

# m = np.array(([1,2,5], [4,3,10]), dtype=float)

class Solucion:
    def __init__(self, valores, cc):
        self.valores = valores
        self.cc = cc

    def imprimir(self):
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
	print m
	sx = sum(x)
	sy = sum(y)
	for i in range(n):
		for j in range(0, grado+1):
			for k in range(0, grado+1):
				m[j,k] = m[j,k] + x[i] ** (k+1+j+1-2)
			m[j, grado + 1] = m[j, grado + 1] + (y[i] * (x[i] ** (j+1-1)))
	print m
	r = gj.Solucion()
	r = gj.GaussJordan(m)
	r = r.incognita[]
	print r
	st = 0
	sr = 0
	for i in range(n):
		st = st + ((promy - y[i]) ** 2)
		s = 0
		for j in range(0, grado+1):
			s = s + (r[j] * (x[i] ** (j-1)))
		sr = sr + ((s - y[i]) ** 2)
	if st != 0:
		corr = (np.sqrt(abs((st - sr) / st))) * 100
		return 1
		#dar la Solucion
	else:
		return 2
		#salta error por div 0



polinomial(x,y)


# polinomial(x,y).imprimir