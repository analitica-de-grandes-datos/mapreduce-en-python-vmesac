#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    maximo = 0
    minimo = 1000

    # cada linea de texto recibida es una entrada clave \tabulador valor
    for line in sys.stdin:
        key, val1, val2 = line.split("\t")
        val1 = float(val1)
        val2 = float(val2)

        if key == curkey:
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma clave.
            
            if val1 > maximo:
                maximo = val1
            else:
                maximo = maximo
            
            if val2 < minimo:
                minimo = val2
            else:
                minimo = minimo
        
        else:
            # Se cambio de clave. Se reinicia el acumulador.
            if curkey is not None:
    
                # una vez se han reducido todos los elementos con la misma clave se imprime el resultado en
                # el flujo de salida
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))

            curkey = key
            maximo = val1
            minimo = val2

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))