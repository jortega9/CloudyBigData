import sys
import re

for line in sys.stdin:
    key, value = line.strip().split('\t',1) #para limitar el numero de particiones de la cadena, solo 1 aunque ponga algun tabulador
    print(str(value))