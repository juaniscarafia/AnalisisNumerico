import numpy as np
from numpy.linalg import *

"Ejercicio 5 - Diagonalmente Dominante"
matriz = np.array(([2, (-0.5),   0,   (-1), 0, 20],
              [0, (-1), 0.25, (-0.2), (-0.2), 17],
              [1, 1,   5,   0, 0, 0],
              [0.5, 0, 0.25, (-1), 0, 0],
              [0, 1, (-1) , 0, 4, 0]), dtype=float)

#Iteraciones
iter = 100

class Solucion:
    def __init__(self):
        self.incognita  = None
        self.iteraciones = None

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
        #resultados = resultados[::-1] #Invertir lista
    sol = Solucion()
    sol.incognita = resultados
    #sol.iteraciones = contador
    return sol

if __name__ == '__main__':
    s = GaussJordan(m)
