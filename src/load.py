import sqlite3

def load_raw_to_db(df, db_path="taxi.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("trips_raw", conn, if_exists="replace", index=False)
    conn.close()
