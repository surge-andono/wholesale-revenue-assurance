# Methodology: Revenue Leakage Detection Framework
## Core Strategy: Reconciliation Usage vs Billing

This document outlines the technical and functional framework used to identify revenue gaps within the wholesale telecommunications segment. The primary objective is to ensure that every unit of network traffic is accurately captured, rated, and billed.

---

## 1. The Concept of Reconciliation
Revenue Leakage in telecommunications often occurs in the "gap" between the Network Layer and the Billing Layer. Our methodology employs a **One-to-One CDR (Call Detail Record) Mapping** to identify these discrepancies.



### Data Sources:
* **Network Usage (Hadoop/Big Data):** Acts as the "Ground Truth." It contains raw logs of every call, data session, or SMS that passed through the network.
* **Billing Transactions (Oracle/Mainframe):** Acts as the "Financial Record." It contains the output of the Rating and Charging engine.

---

## 2. ETL-A Pipeline (Extract, Transform, Load, and Audit)

The project follows a modular pipeline to ensure data integrity at every step:

### Step 1: Extraction & Simulation
Since raw telco data is sensitive (NDA compliant), we simulate a high-volume environment:
* Generation of 5,000+ CDRs with realistic attributes (Service type, Volume, Site ID).
* Intentional injection of a **4% leakage rate** to test the detection engine's sensitivity.

### Step 2: Transformation & Standardization
Data from different silos (Network vs. Billing) often have inconsistent formats. We perform:
* **Key Normalization:** Stripping and cleaning `cdr_id` to ensure perfect join keys.
* **Temporal Alignment:** Converting various string timestamps into unified Python `datetime` objects for time-series analysis.
* **Volume Scaling:** Ensuring usage units (MB, Minutes) are consistent across both datasets.

### Step 3: Reconciliation Logic (The Audit)
We use an **Asymmetric Left Join** operation:
* The Network dataset is the primary table.
* The Billing dataset is joined based on the `cdr_id`.
* **Leakage Identification:** Any record where the Billing side returns `NULL` is flagged as **"Unbilled Usage"**.

### Step 4: Financial Valuation
Each leaked record is assigned a "Potential Loss" value based on the service type's tariff (e.g., Roaming carries a higher loss weight than domestic SMS), allowing the business to prioritize recovery efforts.

---

## 3. Diagnostic & Root Cause Analysis (RCA)

Detecting the leak is only half the battle. Our methodology includes automated RCA to categorize the "Why":

1.  **Temporal Pattern Analysis:** By resampling leakage data into hourly buckets, we can identify if the leakage occurred during a specific system downtime or maintenance window.
2.  **Service Segmentation:** Analyzing which service (Voice, Data, Roaming) is most prone to failure, often indicating a misconfiguration in the specific Rating Engine for that service.
3.  **Site-Level Diagnostics:** Mapping errors to specific `site_id` to detect localized network integration issues.

---

## 4. Business Impact & Risk Mitigation
By implementing this automated reconciliation, the organization moves from **Reactive Discovery** (finding leaks months later) to **Proactive Assurance** (detecting leaks within 24 hours).

* **Accuracy:** >99.9% detection of unbilled CDRs.
* **Scalability:** The modular Python structure allows for easy scaling to millions of records.
* **Compliance:** Provides a clear audit trail for internal and external financial auditors.

---
*Note: This framework is a simulation based on industry-standard Revenue Assurance practices used in major telecommunications firms (2017-2022).*
