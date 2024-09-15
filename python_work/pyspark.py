from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Tutorial") \
    .getOrCreate()
