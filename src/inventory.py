import pandas as pd
import sys

def detect_revenue_leakage(df):
    """
    Analyzes dataframe for high-velocity/low-stock items.
    """
    try:
        # Business Logic: Stock < 50 AND Sales > 2
        risk_df = df[
            (df['Inventory Level'] < 50) & 
            (df['Units Sold'] > 2)
        ].copy()
        
        risk_df['Potential_Loss'] = (risk_df['Units Sold'] - risk_df['Inventory Level']) * risk_df['Price']
        return risk_df.sort_values(by='Potential_Loss', ascending=False)
        
    except KeyError as e:
        print(f"[ERROR] Dataframe missing columns: {e}")
        sys.exit(1)