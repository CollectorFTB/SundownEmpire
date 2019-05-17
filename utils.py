import os
import json

DATA_PATH = 'startup'

def get_data_file(file_path):
    file_path = os.path.join(DATA_PATH, file_path)
    with open(file_path, 'r') as data_file:
        return json.load(data_file)
