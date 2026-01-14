import boto3
import os
from moto import mock_aws
from inventory import detect_revenue_leakage # Import your own code
import pandas as pd

# Constants
INPUT_BUCKET = "retail-data-lake"
INPUT_FILE = "daily_sales.csv"

@mock_aws
def run_simulation():
    print("--- STARTING LOCAL SIMULATION ---")
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=INPUT_BUCKET)
    
    # Upload
    local_path = os.path.join("data", INPUT_FILE)
    s3.put_object(Bucket=INPUT_BUCKET, Key=INPUT_FILE, Body=open(local_path, "rb"))
    
    # Download & Process
    obj = s3.get_object(Bucket=INPUT_BUCKET, Key=INPUT_FILE)
    df = pd.read_csv(obj['Body'])
    
    # Run Logic
    report = detect_revenue_leakage(df)
    
    # Save
    report.to_csv("output/restock_manifest.csv", index=False)
    print(f"Success. identified {len(report)} items. Saved to output/.")

if __name__ == "__main__":
    run_simulation()