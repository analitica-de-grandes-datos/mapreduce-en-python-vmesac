#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

elements = []

for row in sys.stdin:
    elements.append(row)

else:
    elements = sorted(
                        elements, 
                        key = lambda data: (data.split()[0], int(data.split()[2]))
                        )
    
    for element in elements:
        sys.stdout.write("{}".format(element))
