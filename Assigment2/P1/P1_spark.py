from cgitb import text
from pyspark import SparkContext
import sys

sc = SparkContext()

file = sys.argv[2]
word = sys.argv[1]

print(str(file))
print(str(word))
textRDD = sc.textFile(file)\
    .filter(lambda line: (" " + word + " ") in (" " + line + " ")) \
    .collect()

for line in textRDD:
    print(line)

#Puedo iterar el textRDD porque collect() me devuelve un array

# Lo de comparar se hace así para que si meto "whale" por ejemplo, no saque las
#líneas con whales o horse-whales por ejemplo. Esto no lo hacíamos con MapReduce
# a si que no se cómo de bien lo hicimos

#Si quisiera ver mas clara la salida puedo guardarlo en un directoria en vez de imprimirlo usando:
# .saveAsTextfile