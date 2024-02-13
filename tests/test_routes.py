import pytest
from py_term_helpers import top_wrap
from server.models import Receipt
from ipdb import set_trace

top_wrap("TESTING ROUTES")

def test_seed_data(seed_data):
    assert len(Receipt.all) > 0

def test_landing_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'LANDED' in response.data

