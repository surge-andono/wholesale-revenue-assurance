import pandas as pd
import os

def run_diagnostics():
    print("Step 4: Performing Diagnostic & RCA...")
    os.makedirs('data/results', exist_ok=True)
    
    df = pd.read_csv('data/processed/reconciliation_results.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 1. Leakage by Service Type
    service_impact = df.groupby('service_type')['potential_loss'].sum().reset_index()
    service_impact.to_csv('data/results/service_impact.csv', index=False)
    
    # 2. Leakage by Time (Hourly Trend)
    hourly_trend = df[df['billing_status'] == 'Unbilled'].resample('h', on='timestamp').size().reset_index(name='leakage_count')
    hourly_trend.to_csv('data/results/leakage_trend.csv', index=False)
    
    # 3. Top Sites with Errors
    site_errors = df[df['billing_status'] == 'Unbilled'].groupby('site_id').size().reset_index(name='err_count')
    site_errors.sort_values(by='err_count', ascending=False).to_csv('data/results/site_errors.csv', index=False)
    
    print("✅ Diagnostic RCA Completed.")

# if __name__ == "__main__":
#     run_diagnostics()