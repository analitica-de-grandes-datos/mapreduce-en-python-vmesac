#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    total = 0
    count = 0

    # cada linea de texto recibida es una entrada clave \tabulador valor
    for line in sys.stdin:
        key, val1 = line.split("\t")
        val1 = float(val1)

        if key == curkey:
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma clave.
            
            total += val1
            count += 1
            
        else:
            # Se cambio de clave. Se reinicia el acumulador.
            if curkey is not None:
    
                # una vez se han reducido todos los elementos con la misma clave se imprime el resultado en
                # el flujo de salida
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, total/count))

            curkey = key
            total = val1
            count = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, total/count))