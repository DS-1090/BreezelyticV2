
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import date_format

#fetch and process records from csv, CASSdb file
def fetchRecords():
    

    #READS WITH CASSANDRA ARE VERYY INEFFICIENT, THEY TAKE A LOT OF TIME, MEMORY, CPU USAGE AND CASSANDRA CONTAINER KEEPS SHUTTING DOWN
    # 

    # spark = SparkSession.builder \
    #     .appName("CassandraSparkIntegration") \
    #     .master("spark://sparkapp:7077") \
    #     .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.5.0") \
    #     .config("spark.cassandra.connection.host", "cassdb") \
    #     .config("spark.cassandra.connection.port", "9042") \
    #     .config("spark.cassandra.auth.username", "admin") \
    #     .config("spark.cassandra.auth.password", "admin") \
    #     .config("spark.executor.memory", "512m") \
    #     .config("spark.driver.memory", "512m") \
    #     .config("spark.executor.cores", "1") \
    #     .getOrCreate()

    # df = spark.read.format('org.apache.spark.sql.cassandra') \
    #     .options(table='pm25', keyspace='aqdata') \
    #     .load()

    # df.show()

    #SO SHIFTED TO READING IT FROM CSV FILE 

     
    spark = SparkSession.builder.appName("RecordsFetch").getOrCreate()

    df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data.csv")



    df = df.withColumn("avg_pm25", df["avg_pm25"].cast(DoubleType()))
    df = df.withColumn("max_pm25", df["max_pm25"].cast(DoubleType()))
    df = df.withColumn("min_pm25", df["min_pm25"].cast(DoubleType()))

    avg_pm25 = df.groupBy("location").avg("avg_pm25")
    max_pm25= df.groupBy("location").max("max_pm25")
    min_pm25= df.groupBy("location").min("min_pm25")
    df = df.withColumn("date", date_format("date", "dd-MM-yyyy"))
   
    print("avg_pm25")
    avg_pm25.show()
    print("max_pm25")
    max_pm25.show()
    print("min_pm25")
    min_pm25.show()
    df = df.drop("location")  
    data = df.toPandas().to_dict(orient="records")

    return data
 



