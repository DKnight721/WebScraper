import pandas as pd


# Load the JSON file
json_file_path = 'cars.json'  # Path to your .json file
excel_file_path = 'cars.csv'  # Desired path for the .xlsx file

# Read the JSON data into a DataFrame
data = pd.read_json(json_file_path)

# Write the DataFrame to an Excel file
data.to_csv(excel_file_path, index=False)

print(f'Data has been written to {excel_file_path}')
