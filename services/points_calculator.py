import math
import re
from py_term_helpers import *
from ipdb import set_trace
from datetime import datetime
from models.receipt_entity import ReceiptEntity


class PointsCalculator:

    def __init__(self, domains_dict: dict):
       self.domains_dict = {
           "retailer_domain": "http//...."
       } 

    # @staticmethod
    def calculate(self, receipt: ReceiptEntity):
        return (
            PointsCalculator.calc_retailer_points(receipt.retailer, self.domains_dict["retailer_dmoin"])
            + PointsCalculator.calc_item_points(receipt.item_list)
            + PointsCalculator.totals_bonuses(receipt.total)
            + PointsCalculator.description_bonus(receipt.item_list)
            + PointsCalculator.odd_day_bonus(receipt.purchase_date)
            + PointsCalculator.time_of_day_bonus(receipt.purchase_time)
        )

    # network req to /retailer-service
    # req: retailer_name: str => /service
    # req: the points for the reatiler-string
    @staticmethod
    def calc_retailer_points(retailer: str, domain_name: str):
        """ 
        post-req to `domain-name` with the body: {retailer: retailer-str}

        # server offline...
        try: 
            .....
        except Error:
            # if there is an error
            


        """
        return len(re.sub("[^0-9a-zA-Z]+", "", retailer))

    @staticmethod
    def calc_item_points(items: list):
        # center_string_stars((items, type(items)))
        return (len(items) // 2) * 5

    @staticmethod
    def totals_bonuses(total: float):
        # center_string_stars((total, type(total)))
        bonus = 0
        if total % 1.00 == 00:
            bonus += 50
        if total % .25 == 0:
            bonus += 25
        return bonus

    @staticmethod
    def description_bonus(items: list):
        return sum(math.ceil(float(item["price"]) * 0.2) for item in items if len(item["shortDescription"].strip()) % 3 == 0)

    @staticmethod
    def odd_day_bonus(purchase_date: datetime.date):
        return 6 if purchase_date.day % 2 != 0 else 0

    @staticmethod
    def time_of_day_bonus(purchase_time: datetime.time):
        return 10 if 14 <= purchase_time.hour < 16 else 0
