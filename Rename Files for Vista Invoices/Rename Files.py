import os
import pandas as pd

# Load Excel file
directory = "Input your souce directory"
file_path = "Input your file path(.xlsx)"  # Update with your Excel file path
df = pd.read_excel(file_path)

# Ensure column names are correct
old_names = df['Document Number']  # Assuming first column has old filenames
new_names = df['Name']  # Assuming second column has new filenames

# # Rename files
for old, new in zip(old_names, new_names):
    old_path = os.path.join(directory, str(old) + ".pdf")
    new_path = os.path.join(directory, str(new) + ".pdf")

    if os.path.exists(old_path):  # Check if file exists
        os.rename(old_path, new_path)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"File not found: {old}")

print("Renaming process completed.")
