# Library Occupancy Forecasting System

## Project Overview
This project aims to build a cloud-based data pipeline to forecast library occupancy levels using historical data. The system focuses on data ingestion, preprocessing, and feature engineering to support future machine learning models.

## Data Source
ASHRAE Great Energy Predictor III dataset  
https://www.kaggle.com/competitions/ashrae-energy-prediction/data

## Pipeline Overview
- Data Ingestion (Batch)
- Data Cleaning and Preprocessing (ETL)
- Exploratory Data Analysis (EDA)
- Feature Engineering

## Repository Structure
data/
- raw/ → original data
- processed/ → cleaned data

notebooks/
- exploratory analysis and testing

src/
- pipeline scripts (ingestion, ETL, features)
## Data Ingestion

The dataset was obtained from the ASHRAE Great Energy Predictor III competition on Kaggle. A batch ingestion approach was used, where CSV files were downloaded locally and then uploaded to Azure Blob Storage.

A storage account was created in Azure, and a container named `raw` was used to store the original data. The following files were uploaded:

- train.csv  
- weather_train.csv  
- building_metadata.csv  

These files represent the raw data layer and are stored without modification for further processing.
## Data Pipeline Overview

This project implements a cloud-based data pipeline using Azure Databricks and Azure Blob Storage, following the medallion architecture approach (bronze, silver, gold).

### Data Ingestion (Bronze Layer)
The dataset was obtained from the ASHRAE Great Energy Predictor III competition on Kaggle. The data was uploaded to Azure Blob Storage in a container named `raw` without modification.

### Data Cleaning (Silver Layer)
A Databricks notebook was used to load the raw data, check for missing values, remove null records, and convert timestamps to the correct format. The cleaned dataset was stored in parquet format in `processed/train_cleaned`.

### Data Enrichment
The cleaned dataset was enriched by joining it with building metadata and weather data. This added important contextual features such as building characteristics and environmental conditions. The enriched dataset was stored in `processed/enriched_dataset`.

### Feature Engineering (Gold Layer)
A final dataset was created by selecting relevant features for machine learning. The dataset includes building information, weather conditions, and energy consumption data. The final dataset was stored in `processed/features_v1`.

This pipeline demonstrates a scalable cloud-based data processing workflow using Databricks and Azure, aligned with the lab exercises.
