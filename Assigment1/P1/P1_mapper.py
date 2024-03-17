import sys
import re

for line in sys.stdin:
    words = re.sub(r'\W+', ' ', line).rstrip().split()

    for word in words:
        if word.lower() == sys.argv[1].lower() :
            print(word.lower() + '\t' + line.rstrip())
            break
    