# Databricks notebook source
# MAGIC %md
# MAGIC # read silver table

# COMMAND ----------

df = spark.table('fraud_catalog.fraud_schema.silver_transactions')

# COMMAND ----------

# MAGIC %md
# MAGIC #  fraud and genuine count

# COMMAND ----------

from pyspark.sql.functions import count
fraud_summary = df.groupBy('Class').agg(count('*').alias('transaction_count'))

# COMMAND ----------

display(fraud_summary)

# COMMAND ----------

# MAGIC %md
# MAGIC # save gold table

# COMMAND ----------

fraud_summary.write.mode('overwrite').saveAsTable('fraud_catalog.fraud_schema.gold_fraud_summary')

# COMMAND ----------

# MAGIC %md
# MAGIC # Calculate Total Transactions

# COMMAND ----------

total_transactions = df.count()
print("Total Transactions:", total_transactions)

# COMMAND ----------

# MAGIC %md
# MAGIC # Calculate Fraud Transactions

# COMMAND ----------

from pyspark.sql.functions import col
fraud_transactions = df.filter(
col("Class") == 1
).count()
print("Fraud Transactions:", fraud_transactions)

# COMMAND ----------

# MAGIC %md
# MAGIC # Calculate Fraud Percentage

# COMMAND ----------

fraud_percentage = (
fraud_transactions / total_transactions
) * 100
print("Fraud Percentage:", fraud_percentage)

# COMMAND ----------

# MAGIC %md
# MAGIC # Average Fraud Amount

# COMMAND ----------

from pyspark.sql.functions import avg
df.filter(
col("Class") == 1
).agg(
avg("Amount").alias("Avg_Fraud_Amount")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Total Fraud Amount

# COMMAND ----------

from pyspark.sql.functions import sum
df.filter(
col("Class") == 1
).agg(
sum("Amount").alias("Total_Fraud_Amount")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Create Visualization

# COMMAND ----------

display(fraud_summary)

# COMMAND ----------

from pyspark.sql.functions import when

fraud_summary_readable = fraud_summary.withColumn(
    "Transaction_Type",
    when(fraud_summary.Class == 0, "Genuine")
    .otherwise("Fraud")
)

display(fraud_summary_readable)