import numpy as np
from numpy.linalg import *

"Ejercicio 1 - Minimos"
matriz = np.array(([0.02, 0.06, 0.05, 0.01, 18.1],
			       [0.05, 0.02, 0, 0, 8.7],
			       [ 0, 0.02, 0.01, 0.06, 18],
                   [ 0.04, 0.03, 0.02, 0.03, 18.9]), dtype=float)

"Ejercicio 1 - Maximos"
# matriz = np.array(([0.02, 0.06, 0.05, 0.01, 24.5],
# 			       [0.05, 0.02, 0, 0, 12.1],
# 			       [ 0, 0.02, 0.01, 0.06, 25],
#                    [ 0.04, 0.03, 0.02, 0.03, 26.1]), dtype=float)

"Ejercicio 2"
# matriz = np.array(([1,-6,1.5,-3],
#               [2.85,-16.95,4.23,-8.31],
#               [-1.3,8,-2.1,4.4]), dtype=float)

"Ejercicio 2 - Distinto orden - prueba"
# matriz = np.array(([2.85, (-16.95), 4.23, (-8.31)],
# 			              [(-1.3), 8,  (-2.1), 4.4]
# 			             ,[ 1, (-6), 1.5 , (-3)]), dtype=float)

"Ejercicio 3"
# matriz = np.array(( [5, 1, -4.01015, 1],
#  , que                   [-1.301525, -0.25,  1.10075, 0.225],
#                     [ 3.751125, -0.801216, -3.002028 , 0.75]), dtype=float)

"Ejercicio 3 - tomando 2 decimales"
# matriz = np.array(( [5, 1, -4.01, 1],
#                     [-1.30, -0.25,  1.10, 0.22],
#                     [ 3.75, -0.80, -3.00 , 0.75]), dtype=float)

"Ejercicio 4"
# matriz = np.array(([1, 1, 1, 1, 96],
# 			       [0.25, 0.3333, 0.5, 0.5, 31],
# 			       [ (-1), (-1), (10), 0, 0],
#                    [ (-1), (-1), (-1), (15), 0]), dtype=float)

"Ejercicio 5 - Diagonalmente Dominante"
# matriz = np.array(([2, (-0.5),   0,   (-1), 0, 20],
#               [0, (-1), 0.25, (-0.2), (-0.2), 17],
#               [1, 1,   5,   0, 0, 0],
#               [0.5, 0, 0.25, (-1), 0, 0],
#               [0, 1, (-1) , 0, 4, 0]), dtype=float)

"Parcial - actividad 2"
# matriz = np.array(([400, 100, 100, 0, 5470],
#               [0, 200, 50, 400, 8500],
#               [(-100), 0, 620, (-100), 0],
#               [0,(-139.2), 0, 100.5, 52]), dtype=float)

"Parcial actividad 2 - condicionamiento"
# matriz = np.array(([399.9999, 99.9999, 99.9999, 0, 5470],
#               [0, 200, 50, 400, 8500],
#               [(-100), 0, 620, (-100), 0],
#               [0,(-139.2), 0, 100.5, 52]), dtype=float)

"Parcial - actividad 3"
matriz = np.array(([10, 7, 8, 7, (-6)],
                   [7, 5, 6, 5, (-5)],
                   [8, 6, 10, 9, (-12)],
                   [7, 5, 9, 10, (-11)]), dtype=float)

"Parcial - actividad 3 - condicionamiento"
# matriz = np.array(([10.009, 7.009, 8.009, 7.009, (-6.0009)],
#                    [7, 5, 6, 5, (-5)],
#                    [8, 6, 10, 9, (-12)],
#                    [7, 5, 9, 10, (-11)]), dtype=float)


#Iteraciones
iter = 100

class Solucion:
    def __init__(self, valor, iteraciones):
        self.incognita  = valor
        self.iteraciones = iteraciones

    def imprimir(self):
        print """================\n=== SOLUCION ===\n================"""
        for i in range(len(self.incognita)):
            print "x" + str(i+1) + ": %.6f \n" % (self.incognita[i])
        print "Iteraciones: ", self.iteraciones

def GaussJordan(m):
    #Metodo Gauss Jordan.
    F = m.shape[0]
    C = m.shape[1]
    contador = 0
    if not ((F == C - 1) or (0 in m.diagonal())):
        print 'verifique los datos'
    else:
        for i in range (F):
            m[i]= m[i]/m[i,i]
            for c in range(F):
                if not i == c:
                    m[c]=m[c]-(m[i]*m[c,i])
                    contador += 1
        resultados = m[:,-1] #guarda la ultima columna en un vector
    sol = Solucion(resultados,contador)
    return sol

def GaussSeidel(m, iter):
    #Metodo Gauss Seidel.
    if not 0 in m.diagonal():
        F = m.shape[0]
        C = m.shape[1]
        if not (F == C - 1) or (0 in m.diagonal()):
            print 'Verifique los datos'
        mi = m[:,:-1]                           #matriz sin los resultados.
        mr = m[:,-1].reshape(1,F)               #matriz de los resultados y convertida en un vector (horizontal).
        xsol = np.zeros((1,F))                  #vector solucion (comienza con todos ceros).
        xsolant = np.full_like(xsol,None)       #vector solucion anterior (comienza vacio).
        c = 0                                   #contador (se usa para verificar las iteraciones)
        while (c < iter) and (not np.allclose(xsol,xsolant, rtol=0.01)):       #verifica las iteraciones y compara si los resultados de las ultimas 2 iteraciones son parecidos.
            c += 1
            xsolant = np.copy(xsol)             #copia la solucion hasta el momento que, antes de entrar al ciclo, pasa a ser la solucion anterior.
            for i in range(F):
                xfila = np.concatenate((mi[i, :i],mi[i, i+1:]))             #guarda la fila actual (sin el elemento de la diagonal principal)
                xvalor = np.concatenate((xsol[0, :i], xsol[0, i+1:]))       #guarda los valores de la solucion (sin el valor del elemento de la diagonal principal)
                xsol[0, i] = ((mr[0, i] - sum(xfila * xvalor)) / mi[i, i])  #calcula la nueva solucion del sistema.
    sol = Solucion(xsol[0,:],c)
    if c >= iter:
        print ("Se ha superado la cantidad maxima de iteraciones...")
        print ("Solucion encontrada hasta el momento en que se supera la cantidad de iteraciones permitidas:")
    return sol

def Determinante(m):
    #Determinante de la matriz.
    matrizdet = np.copy(m)
    matrizdet = matrizdet[:, :-1]
    filas = matrizdet.shape[0]
    columnas = matrizdet.shape[1]
    for f in range(filas):
        maximo = 0
        for c in range(columnas):
            if abs(matrizdet[f,c]) >=  abs(maximo):
                maximo = matrizdet[f,c]
        for c in range(columnas):
            matrizdet[f, c] = matrizdet[f, c]/maximo
    print ("Matriz con Scalling aplicado:")
    print (matrizdet)
    print
    print ("Determinante de la matriz: " + ": %.6f" % (np.linalg.det(matrizdet)))

if __name__ == '__main__':
    seguir= True
    while seguir:
        m = np.copy(matriz)       #Para que cada vez que ejecutes un metodo no queden los resultados en la matriz general.
        print """Seleccione Tipo de metodo:
               1- Gauss Jordan
               2- Gauss Seidel

               3- Determinante

               4- Salir"""
        try:
            n = int(raw_input('Opcion: '))
        except ValueError:
            n = 5       #Si ingresan texto en lugar de numeros, asigno la opcion 5 que no existe y entonces sale porque la opcion no es valida.
        if n == 1:
            GaussJordan(m).imprimir()

        elif n == 2:
            GaussSeidel(m, iter).imprimir()

        elif n == 3:
            Determinante(m)

        elif n == 4:
            seguir= False

        else:
            print
            print('La opcion ingresada no es valida. Intentelo de nuevo por favor.')
            print
