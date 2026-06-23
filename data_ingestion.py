import pandas as pd
import os

# Automatically finds ALL csv files in data/raw folder
files = os.listdir('data/raw')

for file in files:
    if file.endswith('.csv'):
        df = pd.read_csv(f'data/raw/{file}')
        print(f"\n========== {file} ==========")
        print("Rows and Columns:", df.shape)
        print("Column types:")
        print(df.dtypes)
        print("First 5 rows:")
        print(df.head())
        print("Any missing values:")
        print(df.isnull().sum())