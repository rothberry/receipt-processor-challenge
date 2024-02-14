import pytest
from py_term_helpers import top_wrap
from server.models import Receipt
from ipdb import set_trace
from server.helpers import read_json_file
import json

top_wrap("TESTING ROUTES")


def test_seed_data(seed_data):
    assert len(Receipt.all) > 0


def test_landing_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'LANDED' in response.data


def test_receipt_model():
    first_receipt = Receipt.all[0]
    assert first_receipt.retailer == "Target"
    assert first_receipt.purchaseDate == "2022-01-01"
    assert first_receipt.purchaseTime == "13:01"
    assert first_receipt.total == "35.35"
    assert len(first_receipt.item_list) == 5


def test_point_calculators_target():
    """{
        "retailer": "Target", # +6
        "purchaseDate": "2022-01-01", # +6
        "purchaseTime": "13:01", # +0
        "total": "35.35", # No bonus for whole dollar or multiple .25
        "items": [
            {"shortDescription": "Mountain Dew 12PK","price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza","price": "12.25"}, # +12.25 * .2 => roundup(2.45) => +3
            {"shortDescription": "Knorr Creamy Chicken","price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese","price": "3.35"},
            {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ","price": "12.00"} # +12.00 * .2 => roundup(2.4) => +3
        ] # +5 * 5 items /2 => 10
    }"""
    target_receipt = Receipt.all[0]
    assert target_receipt.calc_retailer_points() == 6
    assert target_receipt.calc_item_points() == 10
    assert target_receipt.description_bonus() == 6
    assert target_receipt.odd_day_bonus() == 6
    assert target_receipt.totals_bonuses() == 0
    assert target_receipt.time_of_day_bonus() == 0
    assert target_receipt.points == 28


def test_point_calculators_corner():
    """{
        "retailer": "M&M Corner Market", # +14
        "purchaseDate": "2022-03-20", # +0
        "purchaseTime": "14:33", # +10
        "total": "9.00", # +50 && +25
        "items": [
            {"shortDescription": "Gatorade","price": "2.25"},
            {"shortDescription": "Gatorade","price": "2.25"},
            {"shortDescription": "Gatorade","price": "2.25"},
            {"shortDescription": "Gatorade","price": "2.25"},
        ] # +5 * 4 items /2 => 10
    }"""
    corner_receipt = Receipt.all[1]
    assert corner_receipt.calc_retailer_points() == 14
    assert corner_receipt.calc_item_points() == 10
    assert corner_receipt.description_bonus() == 0
    assert corner_receipt.odd_day_bonus() == 0
    assert corner_receipt.totals_bonuses() == 75
    assert corner_receipt.time_of_day_bonus() == 10
    assert corner_receipt.points == 109


def test_process_receipts(client, post_req_data):
    response = client.post("/receipts/process", json=post_req_data)
    json_response = response.get_json()
    assert "201" in response.status
    assert type(json_response["id"]) is str


def test_process_bad_receipt(client, bad_post_req_data):
    response = client.post("/receipts/process", json=bad_post_req_data)
    json_response = response.get_json()
    assert "400" in response.status
    assert json_response["errors"]


def test_get_receipt(client):
    last_receipt_id = Receipt.all[-1].id
    res = client.get(f"/receipts/{last_receipt_id}/points")
    json_response = res.get_json()
    assert "200" in res.status
    assert json_response["points"] == 31
