import sys

previous = False
countStock = 0
sum = 0

for line in sys.stdin:
    key, value = line.split('\t', 1)

    if key != previous:
        if previous is not False:
            print(previous + '\t' + str(round(sum / countStock,2)))
        previous = key
        countStock = 0
        sum = 0
    countStock = countStock + 1
    sum = sum + float(value)

print(previous + '\t' + str(round(sum / countStock,2)))