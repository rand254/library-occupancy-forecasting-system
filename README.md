# Library Occupancy Forecasting System

## Project Overview
This project focuses on building a cloud-based data pipeline to support forecasting of building energy usage (as a proxy for occupancy) using the ASHRAE dataset. The main objective is to design and implement a scalable pipeline in Azure that handles data ingestion, cleaning, transformation, and exploratory analysis in preparation for future machine learning models.

---

## Data Source
ASHRAE Great Energy Predictor III dataset  
https://www.kaggle.com/competitions/ashrae-energy-prediction/data

---

## Pipeline Overview
The pipeline follows a structured workflow inspired by the medallion architecture:

- Data Ingestion (Batch)
- Data Cleaning and Preprocessing (ETL)
- Data Enrichment (joining multiple datasets)
- Feature Engineering (final dataset creation)
- Exploratory Data Analysis (EDA)

---

## Technologies Used
- Azure Blob Storage (Data Lake)
- Azure Databricks (PySpark)
- Python (Pandas, Matplotlib, Seaborn)
- GitHub (Version Control)

---

## Repository Structure
