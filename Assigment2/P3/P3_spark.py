
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .getOrCreate()

input_file = "./GOOGLE.csv"

df = spark.read.option("header", "true").csv(input_file)
# Para que la primera linea del csv la lea como cabeceras y no valores
df2 = df.withColumn("Close", df["Close"].cast('float'))
avgDf = df2.groupBy(df2["Date"][1:4]).avg("Close").withColumnRenamed("substring(Date, 1, 4)", "Date")
avgDf.sort("Date").show()

