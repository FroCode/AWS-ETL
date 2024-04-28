# Fintech Data Processing and Analysis

## Overview
This project involves extracting Fintech data, loading it into Amazon Redshift, and preparing for further analysis and visualization in Power BI. The data is processed using a Python script that uploads the data to an S3 bucket and then loads it into a Redshift database.

## Project Structure
- `fintech_data_processing.py`: This script handles the connection to AWS services (S3 and Redshift), creates necessary database schema and tables, and performs data loading operations.
- `.env`: A dotenv file to store sensitive credentials like AWS access keys, Redshift database credentials, etc. (Note: This file should not be checked into version control).
- `README.md`: Provides project documentation.

## Setup Instructions
### Prerequisites
- Python 3.x
- AWS Account
- Amazon Redshift Cluster
- Amazon S3 Bucket
- Power BI Desktop for visualization (Upcoming)

### Environment Setup
1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed.
3. Install required Python packages:
   ```bash
   pip install pandas boto3 psycopg2-binary python-dotenv

REDSHIFT_DATABASE=<your_redshift_database>
REDSHIFT_USER=<your_redshift_user>
REDSHIFT_PASSWORD=<your_redshift_password>
REDSHIFT_HOST=<your_redshift_host>
REDSHIFT_PORT=<your_redshift_port>
AWS_ACCESS_KEY_ID=<your_aws_access_key>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
AWS_REGION=<your_aws_region>
S3_BUCKET=<your_s3_bucket_name>
IAM_ROLE_ARN=<your_iam_role_arn>
