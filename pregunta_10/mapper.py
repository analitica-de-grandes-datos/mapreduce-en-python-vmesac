#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
 
    # itera sobre cada linea de codigo recibida a traves del flujo de entrada
    for line in sys.stdin:
        data = line.split()
        letters = data[1].split(',')
        #newdata = []
        for letter in letters:
            #newdata.append(data[0] + '-' + letter)
            sys.stdout.write("{}\t{}\n".format(letter, data[0]))
