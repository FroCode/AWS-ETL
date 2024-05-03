import boto3
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('./.env')

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

# Create schema and table

cursor.execute("CREATE SCHEMA IF NOT EXISTS fintech;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fintech (
    No INTEGER,
    Company VARCHAR(255),
    Valuation_inB DECIMAL(10,2),
    Date_joined VARCHAR(255),
    Year VARCHAR(255),
    Country VARCHAR(100),
    City VARCHAR(100),
    Industry VARCHAR(255),
    Type VARCHAR(100),
    Description VARCHAR(MAX),
    Website TEXT,
    Investor TEXT
);
""")

# Copy data from S3 to Redshift
cursor.execute(f"""
COPY dev.public.fintech FROM 's3://loadingdatafintech/Fintech Unicorn 2021.csv' IAM_ROLE 'arn:aws:iam::905418126921:role/ReadshiftLoadRole'
FORMAT AS CSV DELIMITER ',' QUOTE '"' IGNOREHEADER 1 REGION AS 'eu-central-1'
""")

cursor.close()
conn.close()
print("Data loaded successfully into Redshift.")
