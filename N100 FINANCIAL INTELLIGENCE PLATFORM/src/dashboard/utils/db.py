import sqlite3
import pandas as pd
import streamlit as st
import os

# Define the database path
DB_PATH = 'nifty100.db'

@st.cache_data
def load_data(query):
    """
    Function to fetch data from SQLite database with caching.
    Uses @st.cache_data to prevent redundant database hits.
    """
    if not os.path.exists(DB_PATH):
        st.error(f"Database file not found at {DB_PATH}")
        return pd.DataFrame()
    
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()
    
def get_table_names():
    """
    Utility function to list all tables in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row(0) for row in cursor.fetchall()]
    conn.close()
    return tables

    