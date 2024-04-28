import pandas as pd

# Load the Excel file
file_path = './Data/Fintech_Unicorn.xlsx'
xl = pd.ExcelFile(file_path)

# Save each sheet to a CSV file
sheet_names = xl.sheet_names
for sheet in sheet_names:
    df = xl.parse(sheet_name=sheet)
    csv_file_path = f"{sheet}.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"Saved {sheet} to {csv_file_path}")
