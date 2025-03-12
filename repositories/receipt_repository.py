from py_term_helpers import *
from models.receipt_entity import ReceiptEntity


class ReceiptRepository:
    # * If connected to a db, may not need the repositories as the db and ORM would hold all this data
    def __init__(self):
        self.receipts = {}

    def save(self, receipt: ReceiptEntity):
        self.receipts[receipt.id] = receipt

    def get_by_id(self, receipt_id: str):
        return self.receipts.get(receipt_id)
