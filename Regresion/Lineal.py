import numpy as np

x = np.array([0,1,3,4,6], dtype = float)

y = np.array([1,3,7,9,13], dtype = float)

class Solucion:
    def __init__(self, valores, cc):
        self.valores = valores
        self.cc = cc

    def imprimir(self):
        print """================\n=== SOLUCION ===\n================"""
        for i in range(len(self.valores)):
            print "a" + str(i) + ": %f \n" % (self.valores[i])

        print "Coeficiente de Correlacion: ", self.cc

def lineal(x, y):
	sx = sum(x)
	sy = sum(y)
	n = x.shape[0]
	promx = sx / n
	promy = sy / n
	sxy = sum(x * y)
	sx2 = sum(x ** 2)
	if ((n * sx2) - (sx ** 2) != 0):
		a1 = ((n * sxy) - (sx * sy)) / ((n * sx2) - (sx ** 2))
		a0 = promy - a1 * promx
		st = 0
		sr = 0
		for i in range(n):
			st = st + ((promy - y[i]) ** 2) 
			sr = sr + (((a1 * x[i]) + a0 - y[i]) ** 2)
			if st != 0:
				r = (np.sqrt(abs((st - sr) / st))) * 100
				sol = Solucion([a0, a1], r)
				return sol


if __name__ == '__main__':
    seguir= True
    while seguir:
        print """Seleccione Tipo de metodo:
               1 - Regresion Lineal
               2 - Salir"""
        try:
            n = int(raw_input('Opcion: '))
        except ValueError:
            n = -1      #Si ingresan texto en lugar de numeros, asigno la opcion 5 que no existe y entonces sale porque la opcion no es valida.
        if n == 1:
        	lineal(x,y).imprimir()

        elif n == 2:
        	pass

        elif n == 3:
            seguir= False

        else:
            print
            print('La opcion ingresada no es valida. Intentelo de nuevo por favor.')