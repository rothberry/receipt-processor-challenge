import json
from server.models import Receipt


def read_json_file(file_path):
    file = open(file_path)
    data = json.load(file)
    return data


def create_receipt_from_file(file_path):
    data = read_json_file(file_path)
    try:
        Receipt(data)
        return True
    except:
        print("failed to create receipt", "X")
