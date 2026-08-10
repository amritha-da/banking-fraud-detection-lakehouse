
# Banking Fraud Detection Lakehouse

## Project Overview

This project implements an end-to-end Banking Fraud Detection Lakehouse using Databricks, PySpark, Delta Lake, and Spark ML.

## Problem Statement

Banks process millions of transactions every day. The objective is to identify fraudulent transactions while maintaining high-quality data and generating business insights.

## Architecture

Credit Card Fraud Dataset
→ Bronze Layer
→ Silver Layer
→ Gold Layer
→ Machine Learning
→ Fraud Prediction

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- Spark SQL
- Spark ML
- Logistic Regression
- Unity Catalog

## Bronze Layer

Stores raw transaction data without modifications.

Table:
bronze_transactions

## Silver Layer

Performs:
- Duplicate Validation
- Null Validation
- Schema Validation
- Data Quality Checks

Table:
silver_transactions

## Gold Layer

Generates:
- Fraud vs Genuine Analytics
- Fraud Metrics
- Business Reporting

Table:
gold_fraud_summary

## Machine Learning

Algorithm:
Logistic Regression

Objective:
Predict fraudulent transactions.

## Model Results

AUC Score: 0.97

True Positives: 53
False Positives: 10
True Negatives: 56751
False Negatives: 38

## Project Outcome

Successfully implemented an end-to-end Banking Fraud Detection Lakehouse using Medallion Architecture and Spark ML.
