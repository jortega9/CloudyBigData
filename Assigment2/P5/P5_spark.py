from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

input_file = "./Meteorite_Landings.csv"

df = spark.read.option("header", "true").csv(input_file)
dfFiltered = df.filter(col("mass (g)").isNotNull())

df2 = dfFiltered.withColumn("mass (g)", dfFiltered["mass (g)"].cast('float'))
avg1 = df2.groupBy(df2["recclass"]).avg("mass (g)") \
    .withColumnRenamed("recclass", "Class") 
roundDF = avg1.toDF("Class","Average mass").select("Class", round("Average mass",2))\
        .withColumnRenamed("round(Average mass, 2)", "Average mass")
roundDF.sort("Class").show()