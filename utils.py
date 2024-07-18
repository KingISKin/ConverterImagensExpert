import os
import shutil
import json

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
def load_cache(cache_path):
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as file:
            return json.load(file)
    return {}
def save_cache(cache_path, cache_data):
    with open(cache_path, 'w') as file:
        json.dump(cache_data, file)