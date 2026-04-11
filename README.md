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

## Conclusion For Phase 1
This project demonstrates the implementation of a cloud-based data pipeline using Azure Databricks and Blob Storage. The pipeline successfully processes raw data into a structured dataset suitable for machine learning.

The use of automation, structured data layers, and exploratory analysis ensures that the system is scalable, reproducible, and ready for the next phase of model development.

This is a professional, narrative-style rewrite of your Phase 2 documentation. It transforms your technical notes into a cohesive "Engineering Report" that tells the story of your project—from the initial baseline struggle to the deep-dive troubleshooting of the deployment.

## Phase 2: Model Development, Validation, and Deployment Strategy

Phase 1: Infrastructure and Data Setup
----------------------------------------------------------------------------------------------------------------------
Before starting the machine learning part, I prepared the environment in Azure Machine Learning Studio. Instead of working with local files, I built a cloud-based setup to simulate a real-world MLOps system. First, I created a registered data asset called library_occupancy_final. This allows the data to be stored, versioned, and reused inside Azure instead of uploading files manually every time. This improves data consistency and traceability. Then, I created a Compute Instance (lab-standard-compute) to run all notebooks and experiments. This instance was also used to track experiments using MLflow, which helped me record model performance, parameters, and results.
----------------------------------------------------------------------------------------------------------------------
Phase 2: Model Development and Validation
----------------------------------------------------------------------------------------------------------------------
1. Baseline Model
----------------------------------------------------------------------------------------------------------------------
To evaluate performance properly, I first created a simple baseline model. I used the average occupancy from the training data and applied it to the test data.

Baseline MAE: 3822.78
This baseline helped me understand how much improvement my model should achieve.
----------------------------------------------------------------------------------------------------------------------
2. Model Improvement (Feature Engineering)
----------------------------------------------------------------------------------------------------------------------
Initially, I trained a Random Forest model using only environmental features like temperature and cloud cover. However, the predictions were not accurate and did not improve much over the baseline. This showed that occupancy depends more on time patterns than weather.

To fix this, I added new features:

Hour of the day
Day of the week

These features helped the model learn patterns such as peak hours and busy days. After adding these features, the model performance improved and was able to outperform the baseline.
----------------------------------------------------------------------------------------------------------------------
3. Reproducibility and Model Versioning
----------------------------------------------------------------------------------------------------------------------
To ensure reproducibility, I used MLflow to track:

Data splits
Random seeds
Hyperparameters
Model results

The best model was registered in Azure as:
library_occupancy_rf_model (Version 4)

I also implemented dynamic model selection, where the system automatically selects the latest model version instead of hardcoding it. This ensures that the best model is always used.
----------------------------------------------------------------------------------------------------------------------
Phase 3: Deployment Strategy and Validation
----------------------------------------------------------------------------------------------------------------------
1. Diagnostic History and Engineering Discipline
----------------------------------------------------------------------------------------------------------------------
During the deployment phase, I faced several infrastructure issues. I kept the logs and error outputs from iterations v11 to v14 in the repository to show my debugging process. These logs show how I moved from fixing missing dependencies (Exit Code 100) to correcting issues in the scoring script (main.py). Keeping these failed attempts helps demonstrate the full troubleshooting process and provides clear traceability of the challenges I faced while setting up the Standard_DS3_v2 compute instance.
----------------------------------------------------------------------------------------------------------------------
2. Transition to Dynamic Automation
----------------------------------------------------------------------------------------------------------------------
In iterations v11–v14, model versions were manually hardcoded.This is not efficient because it needs to be updated every time a new model is created. 
 To improve this, I developed a dynamic model selection solution in iteration v15. This script automatically selects the latest model version from the Azure registry, so the system always uses the best available model without manual changes. 
I have opted to leave the v15 deployment logic as a "Showcase Cell" to demonstrate the automated pipeline design without overwriting the diagnostic history of the previous versions.
----------------------------------------------------------------------------------------------------------------------
3. Final Functional Validation (Plan B)
----------------------------------------------------------------------------------------------------------------------
To confirm the consistency between offline training and production behavior, I performed a final functional test. Through an environment audit in the deployment notebook, I identified a library version discrepancy—where the model was serialized on scikit-learn 1.2.2 while the environment used 1.7.2—causing a binary incompatibility during unpickling.
To verify the model despite this platform constraint, I utilized the Local Inference Validation strategy established in the 05_model_training notebook:
•	Traceability: I pulled the registered Version 4 artifacts directly from the Azure Registry into the local compute memory.
•	Functional Test: By loading the model within the training environment, I produced a table of Actual vs. Predicted values. This successfully confirmed that the model logic is sound and produces accurate results when the environment versions are aligned, proving the model is production-ready.
