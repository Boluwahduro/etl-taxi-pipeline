from extract import extract_data
from load import load_raw_to_db
from transform import run_sql_file

RAW_PATH = "data/raw/yellow_tripdata_2023-01.csv"
DB_PATH = "taxi.db"

def run_pipeline():
    print("Step 1: Extracting data...")
    df = extract_data(RAW_PATH)

    print("Step 2: Loading data into SQLite...")
    load_raw_to_db(df, DB_PATH)

    print("Step 3: Running SQL transformations...")
    run_sql_file(DB_PATH, "sql/transform_trips.sql")

    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
