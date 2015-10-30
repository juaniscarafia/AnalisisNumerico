import numpy as np
import Sistemas_Ecuaciones as gj

#Puntos ingresados
"""
#Ejercicio 1
#Coordenada X
x = np.array([-3,0.5,1,2,5], dtype = float)
#Coordenada Y
y = np.array([-7.5,-2.25,-1.5,0,4.5], dtype = float)
"""
#Ejercicio 2
#Coordenada X
x = np.array([-1,0,2,3,5,6], dtype = float)
#Coordenada Y
y = np.array([6,4,1,1,2,5], dtype = float)

"""
#Ejercicio 3 - Poblacion Urbana
#Coordenada X
x = np.array([0,2,3,4,6,10], dtype = float)
#Coordenada Y
y = np.array([36,32,30,29,28,26], dtype = float)

#Ejercicio 3 - Poblacion Suburbana
#Coordenada X
x = np.array([0,2,3,4,6,10], dtype = float)
#Coordenada Y
y = np.array([4,8.5,9.5,10,11,14], dtype = float)
"""
#Clase Solucion para Metodo Lineal y Polinomial
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
                print "a" + str(i) + ": {:.7g} \n".format(self.valores[i])
            print "Coeficiente de Correlacion: {:.7g} %".format(self.cc)


def lineal(x, y):
    sx = sum(x)
    sy = sum(y)
    n = x.shape[0]
    promx = sx / n
    promy = sy / n
    sxy = sum(x * y)
    sx2 = sum(x ** 2)
    if (n * sx2) - (sx ** 2) != 0:
        a1 = ((n * sxy) - (sx * sy)) / ((n * sx2) - (sx ** 2))
        a0 = promy - a1 * promx
        st = 0
        sr = 0
        for i in range(n):
            st += (promy - y[i]) ** 2
            sr += ((a1 * x[i]) + a0 - y[i]) ** 2
        if st != 0:
            r = (np.sqrt(abs((st - sr) / st))) * 100
            sol = Solucion([a0, a1], r)
        else:
            sol = Solucion(None, None)
        return sol

def polinomial(x, y):
    sy = sum(y)
    n = x.shape[0]
    promy = sy / n
    grado = 0
    while grado < 1:
        try:
            grado = int(raw_input("Ingrese el grado de la funcion: "))
        except ValueError:
            print "El valor ingresado no es valido. Intente nuevamente."
    m = np.zeros((grado + 1,grado + 2))
    for i in range(n):
        for j in range(0, grado+1):
            for k in range(0, grado+1):
                m[j,k] += x[i] ** (k + j)
            m[j, grado + 1] += y[i] * (x[i] ** j)
    # r = gj.Solucion()
    r = gj.GaussJordan(m).incognita
    # r = r.incognita
    st = 0
    sr = 0
    for i in range(n):
        st += (promy - y[i]) ** 2
        s = 0
        for j in range(0, grado+1):
            s += r[j] * (x[i] ** j)
        #sr += ((a1 * x[i]) + a0 - y[i]) ** 2
        sr += (s - y[i]) ** 2
    if st != 0:
        corr = (np.sqrt(abs((st - sr) / st))) * 100
        soluc = Solucion(r, corr)
        #dar la Solucion
    else:
        soluc = Solucion(None, None)
        #salta error por div 0
    return soluc


def lagrange(x, y, valor):
    n = x.shape[0] - 1
    soluc = 0
    for j in range(0, n+1):
        numerador = 1
        denominador = 1
        for i in range(0, n+1):
            if i != j:
                numerador = numerador * (valor - x[i])
                denominador = denominador * (x[j] - x[i])
        soluc += y[j] * (numerador/denominador)
    print "La imagen correspondiente a x = {:.7g} es y = {:.7g} \n".format(valor,soluc)

if __name__ == '__main__':
    while True:
        print """Seleccione el metodo a utilizar:
               1 - Regresion Lineal
               2 - Regresion Polinomial
               3 - Interpolacion de Lagrange
               4 - Salir"""
        try:
            n = int(raw_input('Opcion: '))
        except ValueError:
            n = -1      #Si ingresan texto en lugar de numeros
        if n == 1:
            lineal(x, y).imprimir()
        elif n == 2:
            polinomial(x, y).imprimir()
        elif n == 3:
            try:
                valorinterp = float(raw_input("Ingrese el valor a interpolar (o una letra para salir): "))
                lagrange(x, y, valorinterp)
            except ValueError:
                pass
        elif n == 4:
            if raw_input('Realmente desea salir? Ingrese Y para confirmar, otra letra para continuar: ') == 'Y':
                break
        else:
            print "La opcion ingresada no es valida. Intentelo de nuevo por favor."
