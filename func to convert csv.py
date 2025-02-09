import pandas as pd

def xlsx_to_csv(input_file, output_file, sheet_name=0):
    """
    Convert an XLSX file to CSV.
    
    :param input_file: Path to the input XLSX file
    :param output_file: Path to the output CSV file
    :param sheet_name: Sheet name or index to convert (default is first sheet)
    """
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    df.to_csv(output_file, index=False)
    print(f"Conversion successful: {output_file}")

# Example usage
xlsx_to_csv("TIME TABLE W.E.F 3 FEB 2024.xlsx", "output.csv")

