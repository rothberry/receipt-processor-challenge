import pytest
from py_term_helpers import *


def test_create_receipt(service, sample_receipt):
    receipt = service.create_receipt(sample_receipt)
    assert receipt.id is not None
    assert receipt.retailer == sample_receipt.retailer
    assert receipt.total == float(sample_receipt.total)


def test_get_receipt_by_id(service, sample_receipt):
    receipt = service.create_receipt(sample_receipt)
    fetched_receipt = service.get_receipt_by_id(receipt.id)
    assert fetched_receipt is not None
    assert fetched_receipt.id == receipt.id


def test_get_receipt_not_found(service):
    assert service.get_receipt_by_id("kgfdafkbhdfbhkdhkf") is None
