import pandas as pd

# Load the JSON file
json_file_path = 'items.json'  # Path to your .json file
excel_file_path = 'items.xlsx'  # Desired path for the .xlsx file

# Read the JSON data into a DataFrame
data = pd.read_json(json_file_path)

# Write the DataFrame to an Excel file
data.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f'Data has been written to {excel_file_path}')
