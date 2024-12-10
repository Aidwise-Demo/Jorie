import os
import pandas as pd

def calculate_fill_rate(folder_path):
    # Initialize an empty list to store the results
    results = []

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is an Excel file
        if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
            file_path = os.path.join(folder_path, file_name)

            # Read the Excel file
            try:
                excel_data = pd.ExcelFile(file_path)
                # Loop through each sheet
                for sheet_name in excel_data.sheet_names:
                    df = excel_data.parse(sheet_name)
                    total_rows = len(df)  # Total number of rows in the sheet
                    # Calculate the fill rate for each column
                    for column in df.columns:
                        non_null_count = df[column].notnull().sum()  # Number of non-null rows
                        fill_rate = (non_null_count / total_rows) * 100 if total_rows > 0 else 0
                        results.append({
                            'filename': file_name,
                            'sheet': sheet_name,
                            'column': column,
                            'non_null_count': non_null_count,
                            'total_rows': total_rows,
                            'fill_rate': fill_rate
                        })
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

# Specify the folder containing the Excel files
folder_path = r'C:\Users\Pc\OneDrive - Aidwise Private Ltd\Desktop\11.27.2024'

# Get the fill rate data
fill_rate_df = calculate_fill_rate(folder_path)

# Save the output to a CSV file
output_path = os.path.join(folder_path, 'fill_rate_summary.csv')
fill_rate_df.to_csv(output_path, index=False)

print(f"Fill rate summary saved to {output_path}")
