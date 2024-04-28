import pandas as pd
import boto3
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')

# Database and AWS credentials
DATABASE = os.getenv('REDSHIFT_DATABASE')
USER = os.getenv('REDSHIFT_USER')
PASSWORD = os.getenv('REDSHIFT_PASSWORD')
HOST = os.getenv('REDSHIFT_HOST')
PORT = os.getenv('REDSHIFT_PORT')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('AWS_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')
IAM_ROLE_ARN = os.getenv('IAM_ROLE_ARN')

# Establish a session with AWS
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

# S3 resource
s3 = session.resource('s3')

# Connect to Redshift
conn = psycopg2.connect(
    dbname=DATABASE,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)
conn.autocommit = True
cursor = conn.cursor()

# Create schema if it does not exist
cursor.execute("CREATE SCHEMA IF NOT EXISTS fintech_schema;")
conn.commit()  # Ensure the schema creation is committed

# Create table within the schema
cursor.execute("""
CREATE TABLE IF NOT EXISTS fintech_schema.fintech (
    No INTEGER,
    Company_name VARCHAR(255),
    Valuation_inB_D DECIMAL(10,2),
    Date_joined DATE,
    Year INTEGER,
    Country VARCHAR(100),
    City VARCHAR(100),
    Industry VARCHAR(255),
    Type VARCHAR(100),
    Investor VARCHAR(500)
);
""")

# Copy data from S3 to Redshift
copy_sql = f"""
COPY fintech_schema.fintech
FROM 's3://{S3_BUCKET}/Fintech Unicorn 2021.csv'
CREDENTIALS 'aws_iam_role={IAM_ROLE_ARN}'
FORMAT AS CSV
IGNOREHEADER 1
TIMEFORMAT 'auto'
DATEFORMAT 'auto'
BLANKSASNULL
EMPTYASNULL
MAXERROR 10;
"""
cursor.execute(copy_sql)

cursor.close()
conn.close()
print("Data loaded successfully into Redshift.")
