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
