# s30687

# End-to-End Data Platform Project

**Kedro + PySpark + dbt**

## Project Overview

This project implements a complete **data platform pipeline** using three technologies:

- **Kedro** 
- **Apache Spark (PySpark)** 
- **dbt** 

The project processes the **Chicago Crime dataset** and produces aggregated analytical metrics that can be used for crime trend analysis.

The architecture follows a structure:

```
Raw Data (API / CSV)
      |
Kedro Pipeline
      |
Processed Dataset
      |
PySpark Processing
      |
Database Table
crime_aggregated
      |
dbt Models
      |
Final Metrics / Analytical Tables
```

---

# Dataset Description

## Chicago Crime Dataset

The dataset used in this project contains detailed records of reported crimes in the city of Chicago. It is maintained and published by the Chicago Police Department through the Chicago Data Portal.

Each row represents a **single crime incident**.

The dataset includes:

* crime classification
* location information
* administrative district information
* timestamps
* geospatial coordinates

The dataset enables **spatial and temporal analysis of crime patterns** and can be used for tasks such as:

* crime trend analysis
* geographic clustering of crime incidents
* public safety analytics

---

## Key Variables

| Column               | Description                                         |
| -------------------- | --------------------------------------------------- |
| id                   | unique identifier of the crime record               |
| case_number          | police case number assigned to the incident         |
| date                 | date and time when the incident occurred            |
| block                | approximate block location where the crime occurred |
| iucr                 | Illinois Uniform Crime Reporting code               |
| primary_type         | main category of the crime                          |
| description          | detailed description of the crime type              |
| location_description | type of location (residence, street, etc.)          |
| arrest               | indicates whether an arrest was made                |
| domestic             | indicates whether the crime was domestic-related    |
| beat                 | police beat                                         |
| district             | police district                                     |
| ward                 | city council ward                                   |
| community_area       | Chicago community area                              |
| year                 | year of incident                                    |
| latitude / longitude | geographic coordinates                              |

---

## Dataset Source

Chicago Data Portal – Crimes Dataset

[https://data.cityofchicago.org/resource/ijzp-q8t2.csv](https://data.cityofchicago.org/resource/ijzp-q8t2.csv)

API query used in this project:

```
https://data.cityofchicago.org/resource/ijzp-q8t2.csv?$limit=50000
```

---

# Technology Stack

This project follows the **assignment requirement of using one tool from each category**.

| Category                 | Tool                   |
| ------------------------ | ---------------------- |
| Orchestration / Pipeline | Kedro                  |
| Distributed Processing   | Apache Spark (PySpark) |
| Analytics Layer          | dbt                    |

---

# Architecture

The logical architecture of the data pipeline:

```
Chicago Open Data API
        |
Kedro
(fetch + validate + transform)
        |
Processed dataset
(file_path_to_processed_data)
        |
Apache Spark
(data processing + aggregation)
        |
Database
table: crime_aggregated
        |
dbt
(SQL analytics models)
        |
Final analytical tables and metrics
```

Data flows sequentially between the tools:

1. **Kedro** downloads and prepares the dataset
2. **Spark** performs scalable transformations and aggregations
3. **dbt** builds analytical models on top of processed data

# Data Pipeline Stages

## Kedro – Ingestion & Orchestration


Pipeline nodes:

### fetch_data

Downloads dataset from the Chicago Data Portal API.

Output dataset:

```
raw_data
```

Stored at:

```
new-kedro-project\data\01_raw
```



### validate_data

Performs validation checks:

* dataset is not empty
* required columns exist
* row count is above threshold

If validation fails, the pipeline raises an exception.

Output dataset:

```
validated_data.csv
```

Stored at:

```
 new-kedro-project\data\02_intermediate
```

### clean_transform

Performs initial data cleaning:

* Empty or whitespace-only fields are converted to NULL
* removal of missing values   
* removal of duplicates
* column names converted to python syntax

Output dataset:

```
processed_data
```

Stored at:

```
 new-kedro-project\data\03_primary
```

---

Creates an aggregated table showing the most frequent crime categories.

The node:

* groups records by `primary_type`
* counts the number of crimes in each category
* sorts categories by crime count in descending order
* returns the top `k` crime types

Output dataset:

```
metrics_table
```

Stored at:

```
 new-kedro-project\data\04_feature
```
---

### generate_report

Creates a small pipeline report.

Report includes:

* dataset row count
* number of columns
* execution timestamp

Output:

```
report.json
```

Stored at:

```
 new-kedro-project\data\08_reporting
```

---

### Kedro Execution

Run Kedro pipeline:

```
cd new-kedro-project
venv\Scripts\activate
kedro run
```

Successful execution example:

```
Pipeline execution completed successfully.
Nodes executed: fetch_data -> validate_data -> clean_transform -> feature_or_aggregate -> generate_report
```

Evidence of successful run:

```
docs/kedro_success_screenshot.png
```

---

# Apache Spark – Distributed Processing

PySpark performs scalable processing on the dataset produced by Kedro.

Spark reads the **processed dataset generated by Kedro**.

Input dataset:

```
processed_data
```

Example transformations implemented:


### 1. Filtering

Remove invalid or incomplete records.

The pipeline filters out rows where key columns contain null values, such as:

- id
- case_number
- date
- primary_type
- arrest

### 2. Type Casting

Selected columns are converted to appropriate numeric types to ensure correct processing:

- id → LongType
- year → IntegerType

### 3. Derived Columns

Additional binary indicator columns are created:

- arrest_int → 1 if arrest = True, otherwise 0  
- domestic_int → 1 if domestic = True, otherwise 0

These columns allow numerical aggregation in Spark.

### 4. Aggregation

Spark generates aggregated crime statistics grouped by crime category (`primary_type`).

The aggregation calculates:

- **total_crimes** – total number of crimes in each category  
- **avg_arrest_rate** – average arrest indicator for each crime type  

The aggregated dataset is sorted in descending order by the number of crimes.

The cleaned dataset is stored in the PostgreSQL database table:

`crime_aggregated`
---

### Running Spark

```
cd spark
spark_venv\Scripts\activate
python spark_app.py
```

Output Path:
 spark\output\chicago_crimes_agg_csv


---

# dbt – Analytics Layer

dbt builds the **analytics layer** on top of the Spark-generated table.

Input table:

```
crime_aggregated
```

dbt models create final analytical datasets used for reporting.

Example models:

```
models/staging/stg_crime.sql
models/marts/crime_metrics.sql
```


### Running dbt

```
cd dbt/chicago_crime_dbt
dbt run
dbt test
```

Evidence:

```
docs.evidence.png
```
Stored at: 
```
 dbt\chicago_crime_dbt
```

# Reproducibility

The project is designed to be reproducible.

Anyone can reproduce the pipeline by:

cloning the repository
activating the virtual environments
running each stage in order

Execution order:

```
1. Kedro
2. Spark
3. dbt
```
