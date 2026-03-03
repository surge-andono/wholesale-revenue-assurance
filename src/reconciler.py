import pandas as pd
import numpy as np

def run_reconciler():
    print("Step 3: Running Reconciliation Audit...")
    
    df_net = pd.read_csv('data/processed/network_usage_clean.csv')
    df_bill = pd.read_csv('data/processed/billing_transaction_clean.csv')
    
    # Core Reconciliation Logic
    df_recon = pd.merge(df_net, df_bill, on='cdr_id', how='left')
    df_recon['billing_status'] = np.where(df_recon['billed_amount'].isnull(), 'Unbilled', 'Billed')
    
    # Calculate Potential Loss
    def get_loss(row):
        if row['billing_status'] == 'Unbilled':
            rate = 150 if row['service_type'] in ['Voice', 'Roaming'] else 50
            return row['usage_volume'] * rate
        return 0
    
    df_recon['potential_loss'] = df_recon.apply(get_loss, axis=1)
    df_recon.to_csv('data/processed/reconciliation_results.csv', index=False)
    
    loss_total = df_recon['potential_loss'].sum()
    print(f"✅ Recon Done. Total Potential Loss Detected: Rp {loss_total:,.0f}")
    
# if __name__ == "__main__":
#     run_reconciler()