from py_term_helpers import center_string_stars


class ReceiptRepository:
    # * If connected to a db, may not need the repositories as the db and ORM would hold all this data
    def __init__(self):
        self.receipts = {}

    def save(self, receipt):
        self.receipts[receipt.id] = receipt

    def get_by_id(self, receipt_id):
        return self.receipts.get(receipt_id)
