import json


def read_json_file(file_path):
    file = open(file_path)
    data = json.load(file)
    return data
