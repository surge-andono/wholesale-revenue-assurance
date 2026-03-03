# Data Storytelling: The Dashboard

This dashboard is designed to answer critical business questions in under 30 seconds.

### 1. Data Integrity Score (The Health Check)
* **Goal**: Measure the percentage of network traffic successfully billed.
* **Narrative**: "Our current integrity score is **96%**. 
  
  Given the scale of Telco operations, a 4% gap represents significant unbilled revenue. 
  
  Our industry target is **>99%**, making this our primary focus for system optimization."

![data integrity score](../data/output/data_integrity_score.png)

### 2. Potential Loss by Service (Prioritization)
* **Goal**: Identify where the most value is being lost.
* **Narrative**: "While Data traffic has the highest volume, **Roaming** contributes the largest share of revenue leakage. 
  
![Potential Loss by Service](../data/output/potential_loss_by_service.png)

  This suggests a synchronization issue with international partner settlement files (TAP files) rather than a local network failure."

### 3. Hourly Leakage Trend (Root Cause Analysis)
* **Goal**: Detect when the system fails.
* **Narrative**: "Notice the sharp spike in leakage at 02:00 AM. 

![Hourly Leakage Trend](../data/output/hourly_leakage_trend.png)

  This correlates exactly with the scheduled billing system backup window. **Recommendation**: We should implement a data buffer or shift the backup schedule to prevent CDR processing timeouts."

### Conclusion
By shifting from manual Excel-based audits to this Python-driven engine, we move from **Reactive Reporting** to **Proactive Revenue Recovery**, directly impacting the company's bottom line.
