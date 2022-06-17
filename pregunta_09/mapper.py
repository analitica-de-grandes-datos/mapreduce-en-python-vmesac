#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

elements = []

for row in sys.stdin:
    elements.append(row)

else:
    elements = sorted(
                        elements, 
                        key = lambda data: (int(data.split()[2]))
                        )

    for element in elements[0:6]:      
        sys.stdout.write("{}".format(element))