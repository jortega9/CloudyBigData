from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

input_file = "./ratings.csv"

df = spark.read.option("header", "true").csv(input_file)

df2 = df.withColumn("rating", df["rating"].cast('float'))
avg1 = df2.groupBy(df2["movieid"]).avg("rating")
avgDF = avg1.toDF("movieid","rating").select("movieid", ceil(col("rating")))
c = avgDF.groupBy(avgDF["CEIL(rating)"]).agg(collect_list(col("movieid"))) \
    .withColumnRenamed("CEIL(rating)", "Range") \
    .withColumnRenamed("collect_list(movieid)", "Movies IDs")
c.sort("Range").show()