import pandas as pd
import os

# First let's see what columns exist in our files
fund_master = pd.read_csv('data/raw/01_fund_master.csv')
nav_history = pd.read_csv('data/raw/02_nav_history.csv')

# Print column names of both files
print("Columns in fund_master:")
print(fund_master.columns.tolist())

print("\nColumns in nav_history:")
print(nav_history.columns.tolist())

# Check missing values in all files
print("\n===== MISSING VALUES IN ALL FILES =====")
files = os.listdir('data/raw')
for file in files:
    if file.endswith('.csv'):
        df = pd.read_csv(f'data/raw/{file}')
        missing_vals = df.isnull().sum().sum()
        print(f"{file}: {missing_vals} missing values")