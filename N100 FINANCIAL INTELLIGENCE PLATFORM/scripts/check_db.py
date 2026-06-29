import sqlite3
import pandas as pd
import os

db_path = os.path.join("nifty100.db")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("No tables found in the database.")
    else:
        print(f"Found {len(tables)} tables in the database:")
        for table in tables:
            table_name = table[0]
            print(f"\n--- Table: {table_name} ---")
            df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 0", conn)
            print("Columns:", list(df.columns))
            
    conn.close()
except Exception as e:
    print(f"Error: {e}")