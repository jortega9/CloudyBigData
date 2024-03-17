
from pyspark import SparkContext

sc = SparkContext()

input_file = "./access_log"

textRDD = sc.textFile(input_file)\
    .map(lambda line: line[line.index('"') + 1 : line.rindex('"')])\
    .filter(lambda line: len(line) > 1)\
    .map(lambda url: url.replace(url.split(' ', 1)[0], '', 1))\
    .map(lambda url: (url.strip(), 1))\
    .reduceByKey(lambda x, y: x + y)\
    .saveAsTextFile("salida.txt")

