# Methodology: Data Integrity Framework

This system implements the **ETL-A (Extract, Transform, Load, and Audit)** methodology, specifically tailored for Telecommunications Revenue Assurance.

### 1. Data Ingestion & Generation
The engine simulates two heterogeneous data sources:
* **Network Logs (Hadoop CDR)**: High-volume, unstructured logs representing actual customer usage in the network.
* **Billing Records (Oracle DB)**: Structured financial records processed through rating and charging engines.

### 2. Standardization & Pre-processing
Crucial for handling "noisy" telco data:
* **MSISDN Alignment**: Uniform formatting of subscriber numbers.
* **Temporal Sync**: Aligning timestamps to ISO-8601 standards.
* **Null Handling**: Filtering incomplete CDRs that lack critical usage volume.

### 3. Core Reconciliation Algorithm
Using an **Asymmetric Left-Join Logic**:
* Every network event is mapped against the billing database using a unique `cdr_id`.
* Records without a financial match (Null Join) are flagged as **"Revenue Leakage"**.
* Potential loss is calculated based on simulated dynamic tariffing (e.g., higher rates for Roaming/Voice).

### 4. Diagnostic Analysis (RCA)
Advanced statistical grouping identifies "Why" and "Where" the leakage occurred:
* **Temporal Analysis**: Pinpointing spikes during maintenance windows (batch job failures).
* **Service Segmentation**: Detecting vulnerabilities in specific partner settlement schemes.