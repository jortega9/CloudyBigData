import sys

previous = False
sum = 0

for line in sys.stdin:
    key, value = line.split('\t',1) #para limitar el numero de particiones de la cadena, solo 1 aunque ponga algun tabulador

    if key != previous:
        if previous is not False:
            print(str(sum) + '\t' + previous)
        previous = key    
        sum = 0
    sum = sum + int(value)

print(str(sum) + '\t' + previous)