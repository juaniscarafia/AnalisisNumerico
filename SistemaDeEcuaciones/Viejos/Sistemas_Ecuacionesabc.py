import numpy as np
from numpy.linalg import *

#Matriz
m = np.array(([1, 1,   5,   0, 0, 0],
              [0, 1, (-1) , 0, 4, 0],
              [2, (-0.5),   0,   (-1), 0, 20],
              [0, (-1), 0.25, (-0.2), (-0.2), 17],
              [0.5, 0, 0.25, (-1), 0, 0]), dtype=float)

#Iteraciones
iter = 100

class Solucion:
    def __init__(self, valor):
        self.incognita  = valor

    def imprimir(self):
        print """================\n=== SOLUCION ===\n================"""
        for i in range(len(self.incognita)):
            print "x" + str(i+1) + ": " + str(self.incognita[i]) + "\n"

def GaussSeidel(m, iter):
    #Metodo Gauss Seidel
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
        """En el TP dan el mismo resultado, pero preguntar diferencia entre rtol o atol"""
        while (c < iter) and (not np.allclose(xsol,xsolant, rtol=0.01, atol=0.01)):       #verifica las iteraciones y compara si los resultados de las ultimas 2 iteraciones son parecidos.
            c += 1
            xsolant = np.copy(xsol)             #copia la solucion hasta el momento que, antes de entrar al ciclo, pasa a ser la solucion anterior.
            for i in range(F):
                xfila = np.concatenate((mi[i, :i],mi[i, i+1:]))             #guarda la fila actual (sin el elemento de la diagonal principal)
                xvalor = np.concatenate((xsol[0, :i], xsol[0, i+1:]))       #guarda los valores de la solucion (sin el valor del elemento de la diagonal principal)
                xsol[0, i] = ((mr[0, i] - sum(xfila * xvalor)) / mi[i, i])  #calcula la nueva solucion del sistema.
    sol = Solucion(xsol[0,:])
    if c > iter:
        print ("Se ha superado la cantidad maxima de iteraciones...")
        print ("Solucion encontrada hasta el momento en que se supera la cantidad de iteraciones permitidas:")
    return sol

def GaussJordan(m):
    #Metodo Gauss Jordan
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
    sol = Solucion(resultados)
    return sol

if __name__ == '__main__':
    seguir= True
    while seguir:
        print """Seleccione Tipo de metodo:
               1- Gauss Jordan
               2- Gauss Seidel

               3- Salir"""
        try:
            n = int(raw_input('Opcion: '))
        except ValueError:
            n = 5       #Si ingresan texto en lugar de numeros, asigno la opcion 5 que no existe y entonces sale porque la opcion no es valida.
        if n == 1:
            GaussJordan(m).imprimir()

        elif n == 2:
            GaussSeidel(m, iter).imprimir()

        elif n == 3:
            seguir= False

        else:
            print
            print('La opcion ingresada no es valida. Intentelo de nuevo por favor.')
            print