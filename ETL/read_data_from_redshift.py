import boto3
from io import BytesIO
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv('.env')

# Environment variables for Redshift and AWS
DATABASE = os.getenv('REDSHIFT_DATABASE')
USER = os.getenv('REDSHIFT_USER')
PASSWORD = os.getenv('REDSHIFT_PASSWORD')
HOST = os.getenv('REDSHIFT_HOST')
PORT = os.getenv('REDSHIFT_PORT')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('AWS_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')

# Print the loaded environment variables to confirm they're loaded correctly (optional)
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

object_key = 'Unicorn 2012-2021.csv'  # Ensure this is the correct file name

# Get the object from the bucket
obj = s3.Object(bucket_name, object_key)

# Read the data into a pandas DataFrame
buffer = BytesIO(obj.get()['Body'].read())
df = pd.read_csv(buffer)

# Display the DataFrame
print(df.head())
