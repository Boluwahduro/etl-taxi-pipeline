# ETL Taxi Data Pipeline (SQL + Python)
This project is a beginner-friendly, end-to-end ETL pipeline built using Python, SQL, and SQLite.
It extracts raw NYC Taxi data from a CSV, loads it into a relational database, applies SQL-based data cleaning and transformations, and produces a clean analytical table.

# Pipeline Overview
1. Extract
Load raw NYC taxi trip data from a CSV file using Pandas.
2. Load
Store raw data into a local SQLite database (taxi.db) in a table named trips_raw.
3. Transform
Run SQL scripts that:
Convert timestamps into proper datetime objects
Compute new metrics (trip duration in minutes)
Remove invalid trips (zero passengers, zero distance, negative fares)
Create a clean analytical table trips_clean

# Project Structure
etl-taxi-pipeline/
│
├── data/
│   ├── raw/               # Raw source data (CSV goes here)
│   ├── processed/         # Cleaned outputs
│
├── sql/
│   ├── create_tables.sql  # Defines raw table schema
│   ├── transform_trips.sql # Cleans + transforms the data
│
├── src/
│   ├── extract.py         # Reads CSV into Pandas
│   ├── load.py            # Loads raw data into SQLite
│   ├── transform.py       # Executes SQL transformation scripts
│   ├── pipeline.py        # Orchestrates the ETL workflow
│
├── requirements.txt       # Python dependencies
└── README.md

# How to Run This Pipeline Locally
1. Install dependencies : pip install -r requirements.txt
2. Dowmload dataset: I used the NYC Yellow Taxi trip data (January 2023) https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page and save the CSV file: data/raw/yellow_tripdata_2023-01.csv
3. Run the ETL pipeline from the project root : Run python src/pipeline.py
4. Results: After running: The database file taxi.db will be created and the following tables will exist:

Table	          Description
trips_raw	      Raw imported data
trips_clean	    Cleaned + transformed analytical data

# Tools Used
Python
1. Pandas (Extract step)
2. SQLite3 (Load + DB connection)
SQL
Data cleaning
Type conversion
Date calculations
Data quality filtering

SQLite
Simple, lightweight relational database

