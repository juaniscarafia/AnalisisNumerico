import numpy as np
import math

def funcion(fun,x):
    variable = {'x': x}   
    try:
        return eval(fun,{'math':math},variable)
    except SyntaxError:
        print 'Funcion mal formada'
        return None

def Trapecios(f,a,b):
    return (funcion(f,b) + funcion(f,a))*(b-a)/2.0

def TrapeciosMultiples(f,a,b,n):
    h = (b - a)/n
    i = 1
    suma = 0
    while i != n:
        suma += funcion(f,(a + i*h))
        i += 1
    return (h/2.0)*(funcion(f,a) + 2 * suma + funcion(f,b))

def SimpsonSimple(f,a,b):
    h = (b - a)/2.0
    return (h/3.0)*(funcion(f,a) + 4 * funcion(f,(a+h)) + funcion(f,b))

def SimpsonMultiples(f,a,b,n):
    h = (b - a)/n
    i = 1
    suma = 0
    while i != n:
        if (-1)**i > 0:
            suma += 2 * funcion(f,(a + i*h))
        else:
            suma += 4 * funcion(f,(a + i*h))
        i += 1
    return (h/3.0) * (funcion(f,a) + suma + funcion(f,b))

func = 'x**3 + 2'
x0 = 0.0
xn = 2.0
intervalos = 10.0

print Trapecios(func,x0,xn)
print TrapeciosMultiples(func,x0,xn,intervalos)
print SimpsonSimple(func,x0,xn)
print SimpsonMultiples(func,x0,xn,intervalos)
