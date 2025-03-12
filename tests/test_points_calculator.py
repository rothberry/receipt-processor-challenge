import pytest
from services.points_calculator import PointsCalculator
from utils.validators import *


def test_calc_retailer_points(sample_receipt):
    assert PointsCalculator.calc_retailer_points(
        sample_receipt.retailer) == len("BestBuy")


def test_calc_item_points(sample_receipt):
    assert PointsCalculator.calc_item_points(sample_receipt.item_list) == 5  # 2 items → 5 points


def test_totals_bonuses(sample_receipt):
    assert PointsCalculator.totals_bonuses(100.00) == 75  # Ends in .00
    assert PointsCalculator.totals_bonuses(25.25) == 25  # Ends in .25
    assert PointsCalculator.totals_bonuses(50.23) == 0  # No bonus
    assert PointsCalculator.totals_bonuses(sample_receipt.total) == 0 # 1049.98 


def test_description_bonus(sample_receipt):
    items = [
        # len("Pen") == 3 (multiple of 3)
        {"shortDescription": "Pen", "price": "3.00"},
        # len("Notebook") == 8 (not a multiple of 3)
        {"shortDescription": "Notebook", "price": "10.00"}
    ]
    assert PointsCalculator.description_bonus(items) == 1  # ceil(3.00 * 0.2) = 1
    assert PointsCalculator.description_bonus(sample_receipt.item_list) == 200  # 'laptop % 3; ceil(999.99 * .02) = 200


def test_odd_day_bonus(sample_receipt):
    odd_day = validate_date("2024-03-11")
    even_day = validate_date("2024-03-10")
    assert PointsCalculator.odd_day_bonus(odd_day) == 6  # Odd day
    assert PointsCalculator.odd_day_bonus(even_day) == 0  # Even day
    assert PointsCalculator.odd_day_bonus(sample_receipt.purchase_date) == 0  # Even day


def test_time_of_day_bonus(sample_receipt):
    between_time = validate_time("14:30")
    not_between_time = validate_time("00:01")
    assert PointsCalculator.time_of_day_bonus(between_time) == 10  # Between 14:00-16:00
    assert PointsCalculator.time_of_day_bonus(not_between_time) == 0   # Before 14:00
    assert PointsCalculator.time_of_day_bonus(sample_receipt.purchase_time) == 10  # Between 14:00-16:00
