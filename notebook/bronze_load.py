# Databricks notebook source
# MAGIC %md
# MAGIC # **read the csv**

# COMMAND ----------

df = spark.read.format('csv').options(header = 'True').options(inferschema = 'True').load('/Volumes/fraud_catalog/fraud_schema/bronze')

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC # Understand the Dataset

# COMMAND ----------

print('row:' , df.count())
print( 'column:' , len(df.columns))

# COMMAND ----------

# MAGIC %md
# MAGIC # Check Fraud vs Genuine Transactions

# COMMAND ----------

df.groupBy("Class").count().show()

# COMMAND ----------

df.write.format('delta').mode('overwrite').saveAsTable('fraud_catalog.fraud_schema.bronze_transactions')

#catalog.schema.table

# COMMAND ----------

spark.table("fraud_catalog.fraud_schema.bronze_transactions").show(5)