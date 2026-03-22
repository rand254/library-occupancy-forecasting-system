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
data/

raw/ → original data
processed/ → cleaned and transformed data

notebooks/

01_load_and_clean.ipynb
02_enrich_with_metadata_project.ipynb
03_write_gold_features_v1_project.ipynb
04_exploratory_analysis.ipynb

src/

reserved for future pipeline scripts

---

## Data Ingestion (Bronze Layer)
The dataset was downloaded from Kaggle and uploaded manually to Azure Blob Storage using a batch ingestion approach.

A storage account was created, and a container named `raw` was used to store the original files:

- train.csv  
- weather_train.csv  
- building_metadata.csv  

These files were stored without modification and represent the raw data layer.

---

## Data Cleaning (Silver Layer)
The first Databricks notebook (`01_load_and_clean`) was used to:

- Load raw CSV files using Spark
- Inspect schema and data structure
- Handle missing values (drop nulls)
- Convert timestamp column to proper format

The cleaned dataset was saved in Parquet format in:
processed/train_cleaned

---

## Data Enrichment
In the second notebook (`02_enrich_with_metadata_project`), the cleaned dataset was enriched by joining it with:

- Building metadata  
- Weather data  

This step added important contextual features such as:
- building characteristics (size, usage)
- environmental conditions (temperature, wind, etc.)

The enriched dataset was saved in:
processed/enriched_dataset
---

## Feature Engineering (Gold Layer)
In the third notebook (`03_write_gold_features_v1_project`), a final dataset was created by selecting relevant features for analysis and future modeling.

The dataset includes:
- Building information
- Weather features
- Energy consumption (`meter_reading`)

The final dataset was stored in:
processed/features_v1

---

## Pipeline Automation (Databricks Job)
To make the pipeline reproducible and automated, a Databricks job was created.

The job includes three sequential tasks:
1. `01_load_and_clean`
2. `02_enrich_with_metadata_project`
3. `03_write_gold_features_v1_project`

Each task runs on the same cluster and passes data through the pipeline stages. The pipeline was successfully executed end-to-end, demonstrating automation of the ETL workflow.

---

## Exploratory Data Analysis (EDA)
EDA was performed in the notebook `04_exploratory_analysis` to better understand the dataset.

### Key steps:
- Schema inspection and data preview
- Summary statistics
- Missing value analysis

### Visualizations:

#### 1. Log Distribution of Meter Readings
The original `meter_reading` variable was highly skewed, so a log transformation was applied to better visualize the distribution.

**Insight:**  
Most values are low, with a few very large values, indicating uneven energy usage across buildings.

---

#### 2. Distribution of Meter Types
A bar chart was used to show the distribution of meter types:

- Electricity (most common)
- Chilled water
- Steam
- Hot water

**Insight:**  
Electricity dominates the dataset, meaning most records represent electrical energy usage.

---

#### 3. Correlation Matrix
A correlation matrix was created to analyze relationships between energy consumption and weather variables.

**Insight:**  
- Weak correlation between `meter_reading` and individual weather variables  
- Stronger relationships between some weather features (e.g., air temperature and dew temperature)  
- Indicates that energy consumption depends on multiple factors rather than a single variable  

---

## Conclusion
This project demonstrates the implementation of a cloud-based data pipeline using Azure Databricks and Blob Storage. The pipeline successfully processes raw data into a structured dataset suitable for machine learning.

The use of automation, structured data layers, and exploratory analysis ensures that the system is scalable, reproducible, and ready for the next phase of model development.
