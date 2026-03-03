import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def run_dashboard():
    print("Step 5: Visualizing Integrated Dashboard...")
    os.makedirs('data/output', exist_ok=True)
    
    # Load data
    df_recon = pd.read_csv('data/processed/reconciliation_results.csv')
    service_impact = pd.read_csv('data/results/service_impact.csv')
    leakage_trend = pd.read_csv('data/results/leakage_trend.csv')
    
    # Hitung Skor Integritas
    total = len(df_recon)
    billed = len(df_recon[df_recon['billing_status'] == 'Billed'])
    integrity_score = (billed / total) * 100

    # 1. Membuat Template Subplots (2 baris, 2 kolom)
    # Baris 1: Gauge (Integritas) & Bar Chart (Loss per Service)
    # Baris 2: Line Chart (Hourly Trend) - Merentang di 2 kolom
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "indicator"}, {"type": "bar"}],
               [{"colspan": 2, "type": "scatter"}, None]],
        subplot_titles=("Data Integrity Score", "Potential Loss by Service", "Hourly Leakage Trend (RCA)")
    )

    # 2. Tambahkan Gauge Chart
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=integrity_score,
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "darkblue"}},
        number={'suffix': "%"}
    ), row=1, col=1)

    # 3. Tambahkan Bar Chart
    fig.add_trace(go.Bar(
        x=service_impact['service_type'],
        y=service_impact['potential_loss'],
        marker=dict(color=service_impact['potential_loss'], colorscale='Reds'),
        name="Loss IDR"
    ), row=1, col=2)

    # 4. Tambahkan Line Chart (Trend)
    fig.add_trace(go.Scatter(
        x=leakage_trend['timestamp'],
        y=leakage_trend['leakage_count'],
        mode='lines+markers',
        name="Leakage Count",
        line=dict(color='firebrick', width=3)
    ), row=2, col=1)

    # 5. Update Layout (Styling)
    fig.update_layout(
        title_text="Wholesale Revenue Assurance - Executive Summary",
        height=800,
        showlegend=False,
        template="plotly_white"
    )

    # Tampilkan 1 Dashboard Terpadu
    fig.show()
    
    # Simpan sebagai file HTML (opsional, agar bisa dibuka tanpa Python)
    fig.write_html("data/output/integrated_dashboard.html")
    print("✅ Integrated Dashboard displayed & saved to data/output/integrated_dashboard.html")

# if __name__ == "__main__":
#     run_dashboard()