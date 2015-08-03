# -*- coding: utf-8 -*-
import math
from math import *

'''function that takes a function as a parameter
and a point at which you want to know its value'''
def EvaluateFunction(f,x):
	dic = 	{
				'math':math, 'sin':math.sin,'cos':math.cos,
				'asin': math.asin, 'acos': math.acos,
				'tan': math.tan, 'atan':math.atan,
				'e': math.e, 'pi': math.pi, 'log': math.log,
			}
	return float (eval(f,dic,{'x':x}))

#Enter a function, a quantity and tolerance
function = raw_input('Introducir la función a evaluar: ')
quantity = raw_input('Introducir la cantidad: ')
tolerance = float (raw_input('Introducir la tolerancia: '))

#Enter value xi and xd
xi = float(raw_input('Ingresar valor xi: '))
xd = float(raw_input('Ingresar valor xd: '))

#Function evaluated at points xi and xd
fxi = EvaluateFunction(function, xi)
fxd = EvaluateFunction(function, xd)
count = 0

while (fxi*fxd) > 0:
	#Enter value xi and xd
	xi = float(raw_input('Ingresar valor xi: '))
	xd = float(raw_input('Ingresar valor xd: '))

	#Function evaluated at points xi and xd
	fxi = EvaluateFunction(function, xi)
	fxd = EvaluateFunction(function, xd)
	print fxi
	print fxd
	count += 1

if (fxi * fxd) == 0:
	if fxi == 0:
		raiz = xi
		iteration = count
	else:
		raiz = xd
		iteration = count
else:
	count = 0
	xant = 0
	iteration = 0
	flag = True
	while flag:
		count+= 1
		print 'count: ', count
		print 'xi: ', xi, 'xd: ', xd
		xr1 = (xi+xd)/2
		print 'xr1: ', xr1
		Error = float(xr1-xant)/xr1
		print 'Error: ', Error
		fxr1 = EvaluateFunction(function,xr1)
		print 'fxr1: ', fxr1
		if abs(fxr1) < tolerance or count > quantity or Error < tolerance:
			print abs(fxr1)
			print 'tolerance: ', tolerance
			print (abs(fxr1) < tolerance)
			print count > quantity
			print Error < tolerance
			raiz = xr1
			flag = False
			iteration = count
		else:
			print (abs(fxr1) < tolerance)
			print count > quantity
			print Error < tolerance
			print 'fxi: ', fxi
			print 'fxr1: ', fxr1
			if fxi*fxr1 > 0:
				xi = xr1
				print 'xi: ', xi
			elif fxi*fxr1 < 0:
				xd = xr1
				print 'xd: ', xd
			xant = xr1
			print 'xant: ', xant

print 'Finalizo, la funcion analizada fue ',function
print 'Raiz: ', raiz
print 'iteraciones: ', iteration

#'x**3+4*x**2-10'