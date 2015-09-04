from decimal import *
import numpy as np
import math


class Solucion:
    def __init__(self, raiz=None, error=None, iteraciones=0, estado=None):
        self.raiz= raiz
        self.error= error
        self.iteraciones= iteraciones
        self.estado= estado

        
    def actualizar(self, raiz, error, estado):
        self.raiz= raiz
        self.error= error
        self.estado= estado
        
    def imprimir(self):
        print """================\n=== SOLUCION ===\n================"""
        print '%-20s %-4s' % ('Mensaje de salida: ', estados[self.estado])
        if (self.estado != 5 and self.estado != None):
            print '%-20s %-4s' % ('Raiz encontrada: ', '%.6f' % self.raiz)
            print '%-20s %-4s' % ('Error: ',  '%.6f' % self.error)
            print '%-20s %-4d' % ('Iteraciones: ', self.iteraciones)
        print '\n'

##########################################################################################
##########################################################################################
def funcion(f,x):
    variable =   {
                'math':math, 'sin':math.sin,'cos':math.cos,
                'asin': math.asin, 'acos': math.acos,
                'tan': math.tan, 'atan':math.atan,
                'e': math.e, 'pi': math.pi, 'log': math.log,
                'sqrt': math.sqrt, 'exp':math.exp, 'log1p':math.log1p
            }
    return float (eval(f,variable,{'x':x}))   
    try:
        return eval(f,{'math':math},variable)
    except SyntaxError:
        print 'Funcion mal formada'
        return None


        
def Biseccion(f,xi, xd, tolerancia, iteraciones):
    f,xi, xd, tolerancia, iteraciones = str(f),float(xi), float(xd), float(tolerancia), int(iteraciones)
    solucion= Solucion()
    c= 0
    if funcion(f,xi) * funcion(f,xd) < 0:
        xrant= 0        
        while (solucion.estado == None):
            xr= (xi+xd) / 2.0 
            c+= 1
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), c, 0)
            else:
                error= abs((xr - xrant) / xr)

                if error < tolerancia:
                    solucion.actualizar(xr, error, 4)
                elif c == iteraciones:
                    solucion.actualizar(None, None, 3)
                else:
                    xrant= xr
                    
            if (funcion(f,xi) * funcion(f,xr)) < 0:
                xd= xr
            else:
                xi= xr
    
    elif abs(funcion(f,xi)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xi, abs(funcion(f,xi)), 1)
    elif abs(funcion(f,xd)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xd, abs(funcion(f,xd)), 2)
    elif funcion(f,xi) * funcion(f,xd) > 0:
        solucion.actualizar(None, None, 5)
        
    return solucion

##########################################################################################
##########################################################################################

def ReglaFalsa(f, xi, xd, tolerancia=0.0001, iteraciones=100):
    f,xi, xd, tolerancia, iteraciones = str(f),float(xi), float(xd), float(tolerancia), int(iteraciones)
    solucion= Solucion()
    fstr = f
    c= 0
    if funcion(f,xi) * funcion(f,xd) < 0:
        xrant= 0        
        while (solucion.estado == None):

            xr= ((funcion(f,xi)* xd)-(funcion(f,xd)*xi)) / (funcion(f,xi)-funcion(f,xd)) 
            c+= 1
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), c, 0)
            else:
                error= abs((xr - xrant) / xr)

                if error < tolerancia:
                    solucion.actualizar(xr, error, 4)
                elif c == iteraciones:
                    solucion.actualizar(None, None, 3)
                else:
                    xrant= xr
                    
            if (funcion(f,xi) * funcion(f,xr)) < 0:
                xd= xr
            else:
                xi= xr
    
    elif abs(funcion(f,xi)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xi, abs(funcion(f,xi)), 1)
    elif abs(funcion(f,xd)) < tolerancia:
        # la raiz es xi
        solucion.actualizar(xd, abs(funcion(f,xd)), 2)
    elif funcion(f,xi) * funcion(f,xd) > 0:
        solucion.actualizar(None, None, c, 5)
            
    return solucion

##########################################################################################
##########################################################################################

def Secante(f, xi, xd,  tolerancia=0.0001, iteraciones=100):
    f,xini1, xini0, tolerancia, iteraciones = str(f),float(xi), float(xd), float(tolerancia), int(iteraciones)
    solucion = Solucion()

    c= 0
    if abs(funcion(f,xini1)) < tolerancia:
        #x1 es raiz
        solucion.actualizar(xini1, abs(funcion(f,xini1)), 1)
    elif abs(funcion(f,xini0)) < tolerancia:
        #x2 es raiz
        solucion.actualizar(xini0, abs(funcion(f,xini0)), 2)
    else:     
        while (solucion.estado == None):
            xr= xini1 - ((funcion(f,xini1)*(xini0-xini1)) / (funcion(f,xini0)-funcion(f,xini1)))
            error= abs((xr - xini1) / xr)
            c+= 1
            solucion.iteraciones += 1
            if abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), 0)
            elif error < tolerancia:
                solucion.actualizar(xr, error, 4)
            elif c == iteraciones:
                solucion.actualizar(None, None, 3)
            else:
                xini0= xini1
                xini1= xr
                    
    return solucion

##########################################################################################
##########################################################################################

def Tangente(f, xi, tolerancia= 0.0001, iteraciones= 100):
    f,xi, tolerancia, iteraciones = str(f),float(xi), float(tolerancia), int(iteraciones)
    def df(f,x):
        return ( funcion(f,(x +0.00001))- funcion(f, x))/ 0.00001
    solucion = Solucion()
    
    c= 0
    if abs(funcion(f,xi)) < tolerancia:
        #x1 es raiz
        solucion.actualizar(xi, abs(funcion(f,xi)), 1)
    else:     
        while (solucion.estado == None):
            derivada= df(f,xi)
            if derivada != 0:
                c+= 1
                solucion.iteraciones += 1
                xr= xi - (funcion(f,xi)/derivada)
                error= abs((xr - xi) / xr)

            if derivada == 0:
                solucion.actualizar(None, None, 6) 
            elif abs(funcion(f,xr)) < tolerancia:
                solucion.actualizar(xr, funcion(f,xr), 0)
            elif error < tolerancia:
                solucion.actualizar(xr, error, 4)
            elif c == iteraciones:
                solucion.actualizar(None, None, 3)
            else:
                xi= xr

    return solucion

##########################################################################################
##########################################################################################

def PuntoFijo():
    solucion = Solucion()

    return solucion

estados = {0: 'Se encontro la raiz de la funcion.',
           1: 'La raiz de la funcion es xi.',
           2: 'La raiz de la funcion es xd.',
           3: 'Alcanzo iteraciones maximas.',
           4: 'La diferencia en iteraciones seguidas menor a la tolerancia.',
           5: 'No se puede garantizar que la raiz este entre [xi,xd].',
           6: 'La derivada en un punto de xr = 0',
           None: 'Sin solucion.'}

