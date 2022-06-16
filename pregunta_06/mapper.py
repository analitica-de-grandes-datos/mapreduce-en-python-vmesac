#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        data = line.split()
        sys.stdout.write("{}\t{}\t{}\n".format(data[0], data[2], data[2]))