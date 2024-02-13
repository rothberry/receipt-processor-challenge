import json
from server.models import Receipt


def create_receipt_from_file(file_path):
    file = open(file_path)
    data = json.load(file)
    try:
        Receipt(data)
        return True
    except:
        print("failed to create receipt", "X")
