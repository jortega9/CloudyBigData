import sys

previous = False
countMeteorites = 0
totalMass = 0

for line in sys.stdin:
    type, mass, count = line.split('\t')

    if type != previous:
        if previous is not False:
            print(previous + '\t' + str(round(totalMass / countMeteorites,2)))
        previous = type
        countMeteorites = 0
        totalMass = 0
    countMeteorites += int(count)
    totalMass += float(mass)

print(previous + '\t' + str(round(totalMass / countMeteorites,2)))