from utils.validators import validate_string, validate_price, validate_date, validate_time
from py_term_helpers import center_string_stars
from ipdb import set_trace

class ReceiptDTO:
    # * The Receipt data transfer object
    def __init__(self, json):
        self.retailer = validate_string(json.get("retailer")) # str
        self.purchase_date = validate_date(json.get("purchaseDate"))  # str YEAR-MO-DA
        self.purchase_time = validate_time(json.get("purchaseTime")) # str HR:MI
        self.item_list = self.validate_items(json.get("items")) # list of items
        self.total = validate_price(json.get("total")) # float
        # center_string_stars((self.retailer, self.purchase_date, self.purchase_time, self.total))

    @staticmethod
    def validate_items(items):
        if not isinstance(items, list) or len(items) == 0:
            raise ValueError("Items list must be a non-empty list")
        for item in items:
            if "shortDescription" not in item or "price" not in item:
                raise ValueError(
                    "Each item must have a 'shortDescription' and 'price'")
            item["price"] = validate_price(item["price"])
        return items
