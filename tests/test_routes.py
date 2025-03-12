import pytest
from py_term_helpers import *

top_wrap("TESTING")


def test_landing_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'LANDED' in response.data


def test_process_receipts(client, post_req_data):
    response = client.post("/receipts/process", json=post_req_data)
    json_response = response.get_json()
    assert "201" in response.status
    assert type(json_response["id"]) is str


def test_process_bad_receipt(client, bad_post_req_data):
    response = client.post("/receipts/process", json=bad_post_req_data)
    json_response = response.get_json()
    assert "400" in response.status
    assert json_response["error"]

@pytest.mark.skip(reason="Can't connect the 2 receipt repo instances")
def test_get_receipt(client, service, sample_receipt):
    receipt = service.create_receipt(sample_receipt)
    res = client.get(f"/receipts/{receipt.id}/points")
    json_response = res.get_json()
    assert "200" in res.status
    assert json_response["points"] == 31


def test_not_found_receipt(client):
    bad_receipt_id = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    res = client.get(f"/receipts/{bad_receipt_id}/points")
    json_response = res.get_json()
    assert "404" in res.status
    assert json_response["error"]
