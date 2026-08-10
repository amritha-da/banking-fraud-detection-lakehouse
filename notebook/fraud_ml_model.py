# Databricks notebook source
df = spark.table("fraud_catalog.fraud_schema.silver_transactions")

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC # Prepare Features

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler
feature_column = [c for c in df.columns if c != "Class"]
assembler = VectorAssembler(inputCols=feature_column, outputCol="features")
data = assembler.transform(df)

# COMMAND ----------

train, test = data.randomSplit([0.8, 0.2],seed=42)

# COMMAND ----------

# MAGIC %md
# MAGIC # train the model

# COMMAND ----------

from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(featuresCol="features", labelCol="Class")
model = lr.fit(train)

# COMMAND ----------

predictions.groupBy("Class", "prediction").count().show()

# COMMAND ----------

predictions = model.transform(test)
display(predictions.select("Class","prediction"))

# COMMAND ----------

from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(
    labelCol="Class"
)

auc = evaluator.evaluate(predictions)

print("AUC =", auc)

# COMMAND ----------

prediction_summary = (
    predictions.groupBy(
        "Class",
        "prediction"
    )
    .count()
)

prediction_summary.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable(
    "fraud_catalog.fraud_schema.gold_prediction_summary"
)

# COMMAND ----------

spark.table(
    "fraud_catalog.fraud_schema.gold_prediction_summary"
).show()