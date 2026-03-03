import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def run_generator():
    print("Step 1: Generating Raw Data...")
    os.makedirs('data/raw', exist_ok=True)
    
    np.random.seed(42)
    total_records = 5000
    
    # Network Data (Hadoop Simulation)
    network_data = pd.DataFrame({
        'cdr_id': [f'TXN_{i:06d}' for i in range(1, total_records + 1)],
        'msisdn': [f'62817{np.random.randint(1000000, 9999999)}' for _ in range(total_records)],
        'service_type': np.random.choice(['Voice', 'Data', 'SMS', 'Roaming', 'Interconnection'], total_records, p=[0.2, 0.4, 0.1, 0.2, 0.1]),
        'usage_volume': np.random.uniform(1, 1000, total_records),
        'timestamp': [datetime(2022, 1, 1) + timedelta(minutes=i) for i in range(total_records)],
        'site_id': [f'SITE_{np.random.randint(1, 100)}' for _ in range(total_records)]
    })
    
    # Billing Data (Oracle Simulation) - Injeksi Leakage 4%
    billing_data = network_data.sample(frac=0.96, random_state=7).copy()
    billing_data['billed_amount'] = np.where(
        billing_data['service_type'].isin(['Voice', 'Roaming']), 
        billing_data['usage_volume'] * 150, 
        billing_data['usage_volume'] * 50
    )
    billing_data = billing_data[['cdr_id', 'billed_amount']]
    
    network_data.to_csv('data/raw/network_usage_raw.csv', index=False)
    billing_data.to_csv('data/raw/billing_transaction.csv', index=False)
    print("✅ Raw Data Generated in data/raw/")
    
# if __name__ == "__main__":
#     run_generator()