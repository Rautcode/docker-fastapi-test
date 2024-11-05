# app/services.py
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")

def check_dataset_exists():
    if not os.path.exists(datafolder):
        os.mkdir(datafolder)
    if not os.path.exists(datasource):
        with open(datasource, "w") as f:
            f.write('{"data": []}')  # Initialize with empty JSON structure
            
def read_usersdata():
    check_dataset_exists()
    with open(datasource, "r") as f:
        content = f.read()
        if content == "":
            content = '{"data": []}'  # Fallback if empty
        users = json.loads(content)
    return users

def add_userdata(user: dict):
    users = read_usersdata()
    
    # Add user to the list
    users["data"].append(user)

    # Write back to JSON file
    with open(datasource, "w") as f:
        data = json.dumps(users, indent=2)
        f.write(data)
