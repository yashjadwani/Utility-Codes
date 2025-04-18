import os

def list_folders(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return []
    
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

# Usage
#folders = list_folders("C:/Users/YashJadwani/Game Changer Performance Centre Ltd/PFA SGP and Triage - Documents/General/PFA Triage/Completed Triage Assessments")
#folders = list_folders("C:/Users/YashJadwani/Downloads/Patient Files/Move Files")
print("Folders:", folders)
