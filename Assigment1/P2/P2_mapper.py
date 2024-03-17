import re
import sys

for line in sys.stdin:
    ini = line.index('"')
    fin = line.rindex('"')
    cad = line[ini + 1 : fin]
    if(cad[0] != "-") :
        words = cad.split(' ',1)
        cad1 = cad.replace(words[0], '', 1)
        print(cad1 + "\t1")
    else :
        print(cad + "\t1")

