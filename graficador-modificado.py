import pylab as pl
from numpy import *

# -----------------------------------------------
# Parametros de entrada
# -----------------------------------------------
xmin= -100
xmax= 100
intervalos= 500
# -----------------------------------------------

# Se debe conocer el valor minimo y maximo de 'y' en el intervalo a graficar
ymin= inf
ymax= -inf

# ---------------------------------------------------------------------------------------------
# Graficar funciones
#
# Colores (color) = b:azul; g:verde; r:rojo; c:cyan; m:magenta; y:amarillo; k:negro; w:blanco
# Tipo de Linea (linestyle) = '-':continua; '--':con rayas '-.': rayas y puntos; ':':punteada
# Nombre de referencia (label)
# ---------------------------------------------------------------------------------------------


# Funcion 'R'
f=lambda x: (x**5 -1) * e**x +2
#lambda x: math.log1p(x) 
#(x**2/60)-((x**3*e**-x)/12)-2
#lambda x: (math.log1p(x) + (1 / x)) - 3
#lambda x: (x**5 -1) * e**x +2
#

x= linspace(xmin, xmax, intervalos)
y= f(x)
pl.plot(x,y, color='r', linestyle='--', label='r')
ymin= minimum(ymin, y.min())
ymax= maximum(ymax, y.max())


#-----------------------------------------------------------------------------------------------



# -------------------------------------------------------------------
# Parametros de pyLab extras para que muestre detalles, referencias
# y establezaca los limites de acuerdo a nuestras funciones
# --------------------------------------------------------------------

pl.title('Titulo de la grafica')

pl.xlim(xmin*1.1, xmax*1.1)
pl.ylim(ymin*1.1, ymax*1.1)

pl.grid(True)

    
pl.legend(loc='upper left')

# ejes e intervalos
ax= pl.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
    
# Agrega un titulo y maximiza la figura
mng = pl.get_current_fig_manager()
mng.window.state('normal')

pl.legend(loc='upper left')


# Mostrar la figura
pl.show()
