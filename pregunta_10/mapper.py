#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    
    # itera sobre cada linea de codigo recibida a traves del flujo de entrada
    for line in sys.stdin:
        data = line.split()
        letters = data[1].split(',')
        sys.stdout.write("{},{}\n".format(data[0], letters))