# Databricks notebook source
# MAGIC %md
# MAGIC # read data from bronze

# COMMAND ----------

df = spark.table('fraud_catalog.fraud_schema.bronze_transactions')

# COMMAND ----------

print('rows:' , df.count())

# COMMAND ----------

# MAGIC %md
# MAGIC # check for duplicates

# COMMAND ----------

duplicate_count = df.count() - df.dropDuplicates().count()



# COMMAND ----------

display(duplicate_count)

# COMMAND ----------

# MAGIC %md
# MAGIC # create clean dataframe

# COMMAND ----------

df_clean = df.dropDuplicates()

# COMMAND ----------

from pyspark.sql.functions import col, sum
null_check = df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df.columns
])
display(null_check)



# COMMAND ----------

df_clean.groupBy("Class").count().show()

# COMMAND ----------

df_clean.write.mode("overwrite").saveAsTable("fraud_catalog.fraud_schema.silver_transactions")

# COMMAND ----------

spark.table("fraud_catalog.fraud_schema.silver_transactions").show(5)