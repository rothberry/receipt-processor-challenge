from ipdb import set_trace
from py_term_helpers import center_string_stars, star_line
from uuid import uuid4


class Receipt():

    all = []

    def __init__(self, json) -> None:
        self.retailer = json["retailer"]
        self.purchaseDate = json["purchaseDate"]
        self.purchaseTime = json["purchaseTime"]
        self.item_list = json["items"]

        # TODO remove assumption that total == sum of item prices is always correct
        self.total = json["total"]

        self.id = uuid4()
        # self.points = self.calc_total_points()
        self.points = self.calc_total_points()

        self.all.append(self)
        center_string_stars(f"CREATED RECEIPT ID {self.id}")

    def __repr__(self) -> str:
        return f"""id:\t{self.id} \ total:\t{self.total} \ points:{self.points}"""

    def confirm_total(self):
        # Make sure that the provided total is the same as the sum of all the items' price
        pass

    def calc_total_points(self):
        return self.calc_retailer_points() + self.calc_item_points() + self.totals_bonuses() + self.description_bonus() + self.odd_day_bonus() + self.time_of_day_bonus()

    def calc_retailer_points(self):
        # calculates the points given for retailer name
        # 1 point for each alphanumeric character in name
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
        # if trimmer  length of shortDescription on item is multiple of 3
        # bonus of price x .2
        pass

    def odd_day_bonus(self):
        # 6 points if the day in the purchase date is odd.
        pass

    def time_of_day_bonus(self):
        # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        pass
