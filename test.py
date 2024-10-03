
import pandas as pd

def read_excel_file(file_path):
    """
    Reads an Excel file and returns a DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    pd.DataFrame: The data from the Excel file as a DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
# df = read_excel_file('/path/to/your/excel/file.xlsx')
# print(df.head())

file_path = '/Users/sandracascante/Desktop/MLLB/OSA_Copilot/Info_BDApnea_QuironMalaga.xlsx'
df = read_excel_file(file_path)

# Display the first 5 rows of the DataFrame
if df is not None:
    print(df.head())
else:
    print("Failed to read the Excel file.")
   
# Define a dictionary to rename the columns in the Excel file
# column_renames = {
#     'Edad': 'Age',
#     'Talla': 'Height',
#     'Peso': 'Weight',
#     'PerCervical': 'Cervical',
#     # Add more column renames as needed
# }

# # Rename the columns in the DataFrame
# if df is not None:
#     df.rename(columns=column_renames, inplace=True)
#     print("Columns renamed successfully.")
#     print(df.head())
# else:
#     print("Failed to rename columns because the DataFrame is None.")