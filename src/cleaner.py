import pandas as pd
import os

def run_cleaner():
    print("Step 2: Cleaning and Standardizing Data...")
    os.makedirs('data/processed', exist_ok=True)
    
    df_net = pd.read_csv('data/raw/network_usage_raw.csv')
    df_bill = pd.read_csv('data/raw/billing_transaction.csv')
    
    # Standardizing IDs & Types
    df_net['cdr_id'] = df_net['cdr_id'].str.strip()
    df_bill['cdr_id'] = df_bill['cdr_id'].str.strip()
    df_net['timestamp'] = pd.to_datetime(df_net['timestamp'])
    
    # Data Validation
    df_net.dropna(subset=['msisdn', 'usage_volume'], inplace=True)
    
    df_net.to_csv('data/processed/network_usage_clean.csv', index=False)
    df_bill.to_csv('data/processed/billing_transaction_clean.csv', index=False)
    print("✅ Data Cleaned in data/processed/")
    
# if __name__ == "__main__":
#     run_cleaner()