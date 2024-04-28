import boto3
from io import BytesIO
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv('.env')

# Environment variables should be used for sensitive information
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

# Print the loaded environment variables to confirm they're loaded correctly
print("Database:", DATABASE)
print("User:", USER)
print("Password:", PASSWORD)
print("Host:", HOST)
print("Port:", PORT)

# Initialize a session using Boto3 with credentials from the environment variables
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

# Get the S3 resource
s3 = session.resource('s3')

# Specify the bucket and object
bucket_name = S3_BUCKET  # Use the S3 bucket name from your .env
object_key = 'Fintech_Unicorn_2021_Q1-Q2[1].xlsx'  # Ensure this is the correct file name

# Get the object from the bucket
obj = s3.Object(bucket_name, object_key)

# Read the data into a pandas DataFrame
buffer = BytesIO(obj.get()['Body'].read())
df = pd.read_excel(buffer, sheet_name='Fintech Unicorn 2021')  # Make sure the sheet name matches your file

# Display the DataFrame
print(df.head())
