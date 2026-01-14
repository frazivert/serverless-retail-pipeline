\# Serverless Retail Inventory Pipeline



A local simulation of an AWS inventory management system. It ingests daily sales logs, detects potential revenue leakage (stockouts on high-velocity items), and generates a restock manifest.



\## Structure

\- `src/inventory.py`: Core logic for risk analysis (Lambda function code).

\- `src/main.py`: Local execution script using `moto` to mock S3/AWS.

\- `data/`: Sample datasets (sourced from Kaggle).



\## Setup

1\. `pip install -r requirements.txt`

2\. `python src/main.py`

