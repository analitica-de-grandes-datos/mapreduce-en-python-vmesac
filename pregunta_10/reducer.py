#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = ''

    # cada linea de texto recibida es una entrada clave \tabulador valor

    for line in sys.stdin:

        key, val = line.split("\t")
        val = val.strip()

        if key == curkey:
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma clave.
            total = total + ',' + val
            total = total.split(',')
            total = sorted(int(i) for i in total)
            total = ','.join(str(i) for i in total)

        else:
            # Se cambio de clave. Se reinicia el acumulador.
            if curkey is not None:
    
                # una vez se han reducido todos los elementos con la misma clave se imprime el resultado en
                # el flujo de salida
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = val

    sys.stdout.write("{}\t{}\n".format(curkey, total))