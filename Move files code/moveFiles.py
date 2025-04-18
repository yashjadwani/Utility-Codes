import os
import shutil

def sort_files_by_name(source_directory, destination_directory):
    if not os.path.exists(source_directory):
        print("Source directory does not exist!")
        return
    
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)
        
        if os.path.isfile(file_path):
            name_parts = file.split()
            if len(name_parts) >= 2:  # Assuming first file is atleast two words long and it will move it to that folder but won't create the Folder (Needed for particular case study)
                folder_name = f"{name_parts[0]} {name_parts[1].split('.')[0]}"
                folder_path = os.path.join(destination_directory, folder_name)

                if not os.path.exists(folder_path):
                    pass
                else: 
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved {file} to {folder_name} in {destination_directory}")

# Usage
source = "Input Source File path"
destination = "Input Destination File Path"
sort_files_by_name(source, destination)
