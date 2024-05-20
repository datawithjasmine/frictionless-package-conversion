import pandas as pd
import os
from frictionless import describe

file = (input("Please enter file name: "))

if not os.path.exists(file):
    raise FileNotFoundError(f'The {file} file does not exist in this current directory.')
else:
    def create_df(imported_file):
        if imported_file.endswith('csv'):
            df = pd.read_csv(imported_file)
        elif imported_file.endswith('json'):
            df = pd.read_json(imported_file)
        else:
            raise TypeError('This file format is not supported at this time.')
        return df

df_creation = input(f'A DataFrame has been made of {file}. Would you like to see? (yes/no) ').lower()

if df_creation == 'yes':
    df = create_df(file)
    print(df.to_markdown())
else:
    print("OK.")

# cleaning_data = input(f'Would you like to clean the data from {file}? (yes/no) ')







