#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    total = []

    # cada linea de texto recibida es una entrada clave \tabulador valor
    for line in sys.stdin:

        val, key = line.split(",")
        val = int(val)

        if key == curkey:
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma clave.
            total = sorted(total)
            #elements = sorted(elements, key = lambda data: data.split(",")[3])
        else:
            # Se cambio de clave. Se reinicia el acumulador.
            if curkey is not None:
                # una vez se han reducido todos los elementos con la misma clave se imprime el resultado en el flujo de salida
                sys.stdout.write("{},{}\n".format(curkey.strip(), total))

            curkey = key
            total = val

    sys.stdout.write("{},{}\n".format(curkey.strip(), total))