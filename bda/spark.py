from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
import os
from clusering import KMeans

os.system("cls")


# Opening spark session and loading data into dataframe
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("K-Means") \
    .getOrCreate()
df = spark.read.csv("bda/data.csv", header=True)


points = list()
for row in df.rdd.collect():
    x_cord = row.x
    y_cord = row.y
    points.append([x_cord, y_cord])



kmeans = KMeans(points, 6)
centers_points = kmeans.cluster()