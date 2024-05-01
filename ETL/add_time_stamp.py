import pandas as pd
from datetime import datetime

# Step 1: Load your CSV file
df = pd.read_csv('')  # Replace 'yourfile.csv' with the path to your CSV file

# Step 2: Add a new column with today's date
df['Today'] = datetime.now().date()

# Step 3: Save the DataFrame back to a new CSV file
df.to_csv('updated_file.csv', index=False)  # 'index=False' to avoid saving with an unnamed index column
