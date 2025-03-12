from utils.validators import *
from py_term_helpers import *
from ipdb import set_trace


class ReceiptDTO:
    # * The Receipt data transfer object
    def __init__(self, json: dict):
        self.retailer = validate_string(json.get("retailer"))  # str
        self.purchase_date = validate_date(json.get("purchaseDate"))  # str YEAR-MO-DA
        self.purchase_time = validate_time(json.get("purchaseTime"))  # str HR:MI
        self.item_list = self.validate_items(json.get("items"))  # list of items
        self.total = self.validate_correct_total(self.item_list, validate_price(json.get("total")))  # float

    @staticmethod
    def validate_items(items: list):
        if not isinstance(items, list) or len(items) == 0:
            raise ValueError("Items list must be a non-empty list")
        for item in items:
            if "shortDescription" not in item or "price" not in item:
                raise ValueError(
                    "Each item must have a 'shortDescription' and 'price'")
            item["price"] = validate_price(item["price"])
        return items

    @staticmethod
    def validate_correct_total(items: list, total: float):
        sum_prices = sum([i['price'] for i in items])
        if sum_prices != total:
            raise ValueError("Prices don't add up")
        return total
