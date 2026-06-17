import pandas as pd
from pathlib import Path
from src.etl.normaliser import normalize_ticker, normalize_year
import logging

# Configure logging to track the loading process
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def load_excel_file(file_path: str, is_core: bool = True) -> pd.DataFrame:
    """
    Reads an Excel file into a pandas DataFrame and applies normalization.
    """
    try:
        # Core files have metadata in row 0, so actual headers start at row 1 (header=1).
        # Supplementary files start headers at row 0.
        header_row = 1 if is_core else 0
        df = pd.read_excel(file_path, header=header_row)
        
        # Normalize the company ticker ID
        if 'company_id' in df.columns:
            df['company_id'] = df['company_id'].apply(normalize_ticker)
        elif 'id' in df.columns and 'companies' in str(file_path).lower():
            # In companies.xlsx, the ticker is stored under the 'id' column
            df['id'] = df['id'].apply(normalize_ticker)
            
        # Normalize the year formats
        if 'year' in df.columns:
            df['year'] = df['year'].apply(normalize_year)
        elif 'Year' in df.columns: 
            df['Year'] = df['Year'].apply(normalize_year)
            
        logger.info(f"Successfully loaded {Path(file_path).name} with {len(df)} rows.")
        return df
        
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return pd.DataFrame()

# Quick test execution block
if __name__ == "__main__":
    print("Testing loader.py...")
    
    # Defining a test file path (Example: profitandloss.xlsx)
    test_file = "data/raw/profitandloss.xlsx"
    
    if Path(test_file).exists():
        test_df = load_excel_file(test_file, is_core=True)
        print("\nFirst 3 rows of the loaded data:")
        print(test_df[['company_id', 'year', 'sales']].head(3))
    else:
        print(f"Error: Could not find {test_file}. Please ensure raw Excel files are placed in the 'data/raw/' directory.")
        
        