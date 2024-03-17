import re
import sys

sys.stdin.readline()

for line in sys.stdin:

    words = line.split(',',6)
    date = words[0].split('-',1)

    price = float(words[4]) 

    print(date[0] + "\t" + str(price))