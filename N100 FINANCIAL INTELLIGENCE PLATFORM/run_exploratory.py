import sqlite3
import pandas as pd

DB_PATH = 'nifty100.db'
SQL_FILE = 'src/etl/exploratory_queries.sql'

def run_queries():
    print("Executing Exploratory SQL Queries on nifty100.db...\n")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()  # Using native sqlite3 cursor
    
    with open(SQL_FILE, 'r') as f:
        sql_content = f.read()
        
    # Split queries by semicolon
    queries = [q.strip() for q in sql_content.split(';') if q.strip()]
    
    for i, query in enumerate(queries, 1):
        print(f"--- Running Query {i} ---")
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            
            if cursor.description:
                # Get column names
                cols = [desc[0] for desc in cursor.description]
                df = pd.DataFrame(rows, columns=cols)
                if df.empty:
                    print("No data returned.")
                else:
                    print(df.to_string(index=False))
            else:
                print("Query executed successfully (no rows to display).")
                
        except Exception as e:
            print(f"Error: {e}")
            
        print("\n" + "="*50 + "\n")
        
    conn.close()

if __name__ == "__main__":
    run_queries()