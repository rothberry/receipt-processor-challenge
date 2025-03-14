from ipdb import set_trace
from py_term_helpers import center_string_stars
from uuid import uuid4


class ReceiptData():
    # * ReceiptData will represent the database model
    # * .all would represent a query to select all from the receipt table
    # * for this the `.all` will be a dict of {id: points} for O(1) lookup by id
    all = {}

    def __init__(self, points):
        self.id = str(uuid4())
        self.points = points
        ReceiptData.all[self.id] = self.points

    @classmethod
    def find_receipt(cls, query_id):
        try:
            return cls.all[query_id]
        except KeyError:
            return False

    

class Receipt():

    def __init__(self, json) -> None:
        self.retailer = json["retailer"]
        self.purchaseDate = json["purchaseDate"]
        self.purchaseTime = json["purchaseTime"]
        self.item_list = json["items"]

        # * For the total, we can assume that the given total is always correct
        # self.total = json["total"]
        # * or confirm the total based off of the list of items
        self.total = self.set_total(json["total"])
        self.id = str(uuid4())
        self.points = self.calc_total_points()

        self.all.append(self)
        print("")
        center_string_stars(f"CREATED RECEIPT ID {self.id}")

    def __repr__(self) -> str:
        return f"""||id:\t{self.id} | total:\t{self.total} | points:{self.points}||"""

    def set_total(self, given_total):
        item_total = 0
        for item in self.item_list:
            item_total = round(item_total + float(item["price"]), 2)
        if item_total == float(given_total):
            return given_total
        else:
            # * Could go 2 ways if the totals don't match:
            # * 1. Error out
            raise AssertionError(
                "Total and calculated item total do not match")
            # * 2. Overwrite the provided total with the calculated total
            # return str(item_total)

    def calc_total_points(self):
        return self.calc_retailer_points() + self.calc_item_points() + self.totals_bonuses() + self.description_bonus() + self.odd_day_bonus() + self.time_of_day_bonus()

    def calc_retailer_points(self):
        # * calculates the points given for retailer name
        # * 1 point for each alphanumeric character in name
        import re
        alnum_str = re.sub("[^0-9a-zA-Z]+", "", self.retailer)
        return len(alnum_str)

    def calc_item_points(self):
        # gives 5 per every 2 items in item_list
        return len(self.item_list) // 2 * 5

    def totals_bonuses(self):
        # gives bonus if total is XX.00
        # AND
        # gives bonus if total multiple of .25
        bonus = 0
        change = self.total.split(".")[1]
        if change == "00":
            bonus += 50
        if int(change) % 25 == 0:
            bonus += 25
        return bonus

    def description_bonus(self):
        # if trimmed length of shortDescription on item is multiple of 3
        # bonus of price x .2 rounded up
        import math
        bonus = 0
        for item in self.item_list:
            if len(item["shortDescription"].strip()) % 3 == 0:
                bonus += math.ceil(float(item["price"]) * 0.2)
        return bonus

    def odd_day_bonus(self):
        # 6 points if the day in the purchase date is odd.
        return 6 if int(self.purchaseDate.split("-")[-1]) % 2 != 0 else 0

    def time_of_day_bonus(self):
        # 10 points if the time of purchase is after 14:00 and before 16:00.
        return 10 if int(self.purchaseTime.split(':')[0]) in range(14, 16) else 0
