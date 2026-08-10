# Banking Fraud Detection Lakehouse

## Project Overview

This project implements an end-to-end Banking Fraud Detection Lakehouse using Databricks, PySpark, Delta Lake, and Spark ML.

## Architecture

Bronze → Silver → Gold → Machine Learning

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- Spark SQL
- Spark ML
- Logistic Regression

## Bronze Layer

Stores raw transaction data ingested from the source CSV file.

## Silver Layer

Performs:
- Duplicate validation
- Null checks
- Data quality validation

## Gold Layer

Generates:
- Fraud vs Genuine transaction analysis
- Fraud metrics
- Business-ready analytics

## Machine Learning

Algorithm: Logistic Regression

Objective:
Predict fraudulent transactions using transaction features.

## Results

- AUC Score: 0.97
- True Positives: 53
- False Positives: 10
- True Negatives: 56,751
- False Negatives: 38

## Project Flow

creditcard.csv
→ Bronze Layer
→ Silver Layer
→ Gold Layer
→ Logistic Regression Model
→ Fraud Prediction
