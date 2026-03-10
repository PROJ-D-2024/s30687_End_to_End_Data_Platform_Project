from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, count, avg
)
from pyspark.sql.types import IntegerType, LongType

# # 1. SparkSession
# spark = (SparkSession.builder
#     .appName("ChicagoCrimesSparkAssignment")
#     .master("local[*]")
#     .getOrCreate())

spark = (
    SparkSession.builder
    .appName("ChicagoCrimesSparkAssignment")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3")
    .getOrCreate()
)
print("Spark Session Started")
print("App Name:", spark.sparkContext.appName)
print("Spark Version:", spark.version)


df = spark.read.csv("..\\new-kedro-project\\data\\03_primary\\processed_data.csv", header=True, inferSchema=True)

print("Raw Schema")
df.printSchema()

print("Raw Row Count")
print(df.count())

# 3. Data cleaning & transformations

# a) filter invalid/null rows
df_clean = df.filter(
    col("id").isNotNull() &
    col("case_number").isNotNull() &
    col("date").isNotNull() &
    col("primary_type").isNotNull() &
    col("arrest").isNotNull()
)

# b) cast columns to correct types
df_clean = (df_clean
            .withColumn("id", col("id").cast(LongType()))
            .withColumn("year", col("year").cast(IntegerType())))

# d) remove duplicates
df_clean = df_clean.dropDuplicates(["id", "case_number"])

# e) create derived columns
df_clean = (df_clean
            .withColumn("arrest_int", when(col("arrest") == True, 1).otherwise(0))
            .withColumn("domestic_int", when(col("domestic") == True, 1).otherwise(0)))

print("Schema")
df_clean.printSchema()

print("Sample")
df_clean.select("id","description","arrest").show(10, truncate=False)

# 4. Aggregation
agg_df = df_clean.groupBy("primary_type").agg(
    count("*").alias("total_crimes"),
    avg("arrest_int").alias("avg_arrest_rate"),
).orderBy(col("total_crimes").desc())

agg_df.show(20, truncate=False)

# Optional extra action
print("Number of aggregated groups")
print(agg_df.count())



jdbc_url = "jdbc:postgresql://localhost:5432/nyc"

connection_properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

table_name = "crime_aggregated"

df_clean.write.mode("overwrite").jdbc(jdbc_url, table_name, properties=connection_properties)
output_path = "output/chicago_crimes_agg_csv"
agg_df.write.mode("overwrite").parquet(output_path)

spark.stop()


