import pandas as pd
import os
def load_csv(path):
    
    df = pd.read_csv(path)
    return df
 
def find_file(folder_path, keyword):
     for file in os.listdir(folder_path):
         if keyword in file:
             return os.path.join(folder_path,file)
 
 
 
def load_folder(folder_path):
    folder_data = {}
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            full_path = os.path.join(folder_path, file)
            df = load_csv(full_path)
            kpi_name = file
            folder_data[kpi_name] = df

    return folder_data

def load_project(project_path):
    project_data = {}
    for folder in os.listdir(project_path):
        folder_path = os.path.join(project_path, folder)
        if os.path.isdir(folder_path):
            project_data[folder] = load_folder(folder_path)

    return project_data
	