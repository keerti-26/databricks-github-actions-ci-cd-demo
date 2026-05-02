from pyspark.sql import functions as F

#Reading csv
transaction = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/ecommerce_data_analysis/default/transaction-volume/")

#Cleaning the file
cleaned_transaction = (transaction.filter(F.col("Transaction_ID").isNotNull())
                                .dropDuplicates(subset=["Transaction_ID"])
)

cleaned_transaction.write.format("delta").mode("append").saveAsTable("transaction")