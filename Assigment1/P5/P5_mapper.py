import re
import sys
import csv

with sys.stdin as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['mass (g)'] and row['mass (g)']:
            print(row['recclass'] + '\t' + row['mass (g)'] + '\t1')