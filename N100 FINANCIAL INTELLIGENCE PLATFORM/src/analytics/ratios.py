import sqlite3
import pandas as pd
import numpy as np

class ProfitabilityEngine:
    def __init__(self, db_path='nifty100.db'):
        self.db_path = db_path
        
    def fetch_data(self):
        """
        P&L, Balance Sheet take data in the table.
        """
        query = """
        SELECT
            p.company_id,
            p.year,
            p.sales,
            p.operating_profit,
            p.net_profit,
            p.opm_percentage as source_opm,
            b.equity_capital,
            b.reserves,
            b.borrowings
        FROM profitandloss p
        JOIN balancesheet b
            ON p.company_id = b.company_id AND p.year =b.year
        """
        with sqlite3.connect(self.db_path) as conn:
            df =pd.read_sql_query(query, conn)
        return df
    
    # --- Ratio Calculation Functions ---
    def calc_npm(self, row):
        # Edge Case: Zero Sales
        if pd.isna(row['sales']) or row['sales'] ==0:
            return None
        return round((row['net_profit'] / row['sales']) * 100, 2)
    
    def calc_opm(self, row):
        # Edge Case: Zero Sales
        if pd.isna(row['sales']) or row['sales'] == 0:
            return None
        return round((row['operating_profit'] / row['sales']) * 100, 2)
    
    def calc_roe(self, row):
        equity = row['equity_capital'] + row['reserves']
        # Edge Case: Negative Equity
        if pd.isna(equity) or equity <= 0:
            return None
        return round((row['net_profit'] / equity) * 100 , 2)
    
    def calc_roce(self, row):
        equity = row['equity_capital'] + row['reserves']
        capital_employed = equity + row['borrowings']
        if pd.isna(capital_employed) or capital_employed <= 0:
            return None
        return round((row['operating_profit'] / capital_employed) * 100, 2)
    
    def run(self):
        print("Initializing Profitability Ratio Engine...\n" )
        df = self.fetch_data()
        
        # Calculate all 4 ratios
        df['NPM'] = df.apply(self.calc_npm, axis=1)
        df['OPM'] = df.apply(self.calc_opm, axis=1)
        df['ROE'] = df.apply(self.calc_roe, axis=1)
        df['ROCE'] = df.apply(self.calc_roce, axis=1)
        
        # --- Cross-Validation for OPM ---
        # Tolerance set to +/- 2%
        df['opm_diff']         = abs(df['OPM'] - df['source_opm'])
        mismatches = df[df['opm_diff'] > 2.0]
        
        print(f"Successfully computed ratio for {len(df)} records.")
        print(f"OPM Cross-validation: Found {len(mismatches)} records exceeding 2% tolerance. \n")
        
        if not mismatches.empty:
            print("OPM mismatch sample (calculated vs source):")
            print(mismatches[['company_id', 'year', 'OPM', 'source_opm', 'opm_diff']].head(5).to_string(index=False))
            print("\n")
            
        return df
    
if __name__ == "__main__":
    engine = ProfitabilityEngine()
    result_df = engine.run()
    
    print("Sample Calculated Ratios:")
    print(result_df[['company_id', 'year', 'NPM', 'OPM', 'ROE', 'ROCE']].head(10).to_string(index=False))
            
        
    