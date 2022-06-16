#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        data = line.split(",")
        sys.stdout.write("{},{}\n".format(data[1].strip(), data[0]))

