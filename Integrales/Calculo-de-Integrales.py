import numpy as np
import math

#Funcion
funcioningresada = 'x ** 3 + 2'

#Intervalo
x0 = -1.0
xn = 2.0

#Numero de divisiones/intervalos
intervalos = 11

#Evalua la funcion
def funcion(f, x):
    variable =   {
                'math':math, 'sin':math.sin,'cos':math.cos,
                'asin': math.asin, 'acos': math.acos,
                'tan': math.tan, 'atan':math.atan,
                'e': math.e, 'pi': math.pi, 'log': math.log,
                'sqrt': math.sqrt, 'exp':math.exp, 'ln':math.log,
                }
    return float (eval(f, variable,{'x':x}))   
    try:
        return eval(f, {'math':math}, variable)
    except SyntaxError:
        print 'Funcion mal formada'
        return None

#Metodos
def Trapecios(f, a, b):
    return ((funcion(f, b) + funcion(f, a))*(b - a)) / 2.0

def TrapeciosMultiples(f, a, b, n):
    h = (b - a) / float(n)
    suma = 0
    for i in range(1, n):
        suma += funcion(f, (a + i * h))
    return (h / 2.0) * (funcion(f, a) + 2 * suma + funcion(f, b))

def Simpson1_3Simple(f, a, b):
    h = (b - a) / 2.0
    return (h / 3.0) * (funcion(f, a) + 4 * funcion(f, (a + h)) + funcion(f, b))

def Simpson1_3Multiple(f, a, b, n):
    h = (b - a) / float(n)
    resultadofinal = 0.0
    sumap = 0
    sumai = 0
    if n % 2 != 0:
        b1 = b
        b -= 3 * h
        resultadofinal += Simpson3_8(funcioningresada, b, b1)
        n -= 3
    for i in range(1, n):
        if i % 2 == 0: #Verifica que sea par (True) o impar (False); % calcula el resto de la division
            sumap += funcion(f, (a + i * h))
        else:
            sumai += funcion(f, (a + i * h))
    return (resultadofinal + ((h / 3.0) * (funcion(f, a) + (2 * sumap) + (4 * sumai) + funcion(f, b))))

def Simpson3_8(f, a, b):
    h = (b - a) / 3.0
    return (3 * h / 8.0) * (funcion(f, a) + (3 * funcion(f, (a + h))) + (3 * funcion(f, (a + (2 * h)))) + funcion(f, b))

if __name__ == '__main__':
    while True:
        print """Seleccione el metodo a utilizar:
               1 - Trapecios
               2 - Trapecios Multiples
               3 - Simpson 1/3 Simple
               4 - Simpson 1/3 Multiple
               5 - Salir"""
        try:
            n = int(raw_input('Opcion: '))
        except ValueError:
            n = -1      #Si ingresan texto en lugar de numeros
        if n == 1:
            print "El resultado es: {:.7g}".format(Trapecios(funcioningresada, x0, xn))
        elif n == 2:
            print "El resultado es: {:.7g}".format(TrapeciosMultiples(funcioningresada, x0, xn, intervalos))
        elif n == 3:
            print "El resultado es: {:.7g}".format(Simpson1_3Simple(funcioningresada, x0, xn))
        elif n == 4:
            print "El resultado es: {:.7g}".format(Simpson1_3Multiple(funcioningresada, x0, xn, intervalos))
        elif n == 5:
            break
        else:
             print "La opcion ingresada no es valida. Intentelo de nuevo por favor."