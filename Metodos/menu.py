import metodos_raices as raices


def opcion(msjentrada, msjerror, minopcion, maxopcion, tipodato):
    salir= False

    mincondicion = False    
    maxcondicion = False
    while not salir:
        try: 
            m = tipodato(raw_input(msjentrada))

            if minopcion is None:
                mincondicion= True
            else:
                mincondicion= (m >= minopcion)

            if maxopcion is None:
                maxcondicion= True
            else:
                maxcondicion= (m <= maxopcion)

        except ValueError:
            salir = False
            print msjerror

        salir= mincondicion and maxcondicion
        if salir:
            return m
        else:
            print msjerror


if __name__ == '__main__':
    
    func_str = 'log1p(x) + (1 / x) - 3'
    seguir= True
    while seguir:

        print """Seleccione Tipo de metodo:
               1- Metodos Cerrados
               2- Metodos Abiertos
               
               3- Modificar funcion

               4- Salir"""

        m = opcion('Opcion: ','Numero no valido. Ingrese nuevamente.', 1, 5, int)
        print '\n'
        
        if m == 1:
            print """Seleccione metodo cerrado:
            1- Metodo Biseccion
            2- Metodos Regla Falsa"""

            s= raices.Solucion()

            m = opcion('Opcion: ','Numero no valido. Ingrese nuevamente.', 1, 2, int)            
            print '\n'

            xi = opcion('Ingrese xi: ','Numero no valido. Ingrese nuevamente.', None, None, float)            
            xd = opcion('Ingrese xd: ','Numero no valido. Ingrese nuevamente.', None, None, float)
            tolerancia = opcion('Ingrese tolerancia: ','Numero no valido. Ingrese nuevamente.', None, None, float)
            itermax = opcion('Ingrese iteraciones: ','Numero no valido. Ingrese nuevamente.', None, None, int)
            print '\n'

            if m == 1:            
                s = raices.Biseccion(func_str,xi,xd,tolerancia,itermax)
            elif m == 2:
                s = raices.ReglaFalsa(func_str,xi,xd,tolerancia,itermax)


            #Imprime resultados en pantalla
            s.imprimir()

        elif m == 2:
            print """Seleccione metodo abierto:
            1- Metodo Tangente
            2- Metodos Secante
            3- Metodo Punto Fijo"""

            s= raices.Solucion()

            m = opcion('Opcion: ','Numero no valido. Ingrese nuevamente.', 1, 3, int)
            print '\n'

            if m == 1:
                xi = opcion('Ingrese punto de inicio: ','Numero no valido. Ingrese nuevamente.', None, None, float)
                tolerancia = opcion('Ingrese tolerancia: ','Numero no valido. Ingrese nuevamente.', None, None, float)
                itermax = opcion('Ingrese iteraciones: ','Numero no valido. Ingrese nuevamente.', None, None, int)
                s = raices.Tangente(func_str, xi, tolerancia, itermax)

            elif m == 2:
                xi = opcion('Ingrese punto de inicio 1: ','Numero no valido. Ingrese nuevamente.', None, None, float)
                xd = opcion('Ingrese punto de inicio 2: ','Numero no valido. Ingrese nuevamente.', None, None, float)
                tolerancia = opcion('Ingrese tolerancia: ','Numero no valido. Ingrese nuevamente.', None, None, float)
                itermax = opcion('Ingrese iteraciones: ','Numero no valido. Ingrese nuevamente.', None, None, int)
                s = raices.Secante(func_str,xi,xd,tolerancia,itermax)
                
            elif m == 3:
                s = raices.PuntoFijo()

            s.imprimir()

        elif m == 3:
            bienformada= False
            while not bienformada:
                func_str = opcion('Nueva funcion: ','Error.', None, None, str)
                bienformada = (raices.funcion(func_str , 1)!= None)
                
        elif m == 4:
            seguir= False

        
