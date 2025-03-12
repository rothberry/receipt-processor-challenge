from uuid import uuid4
from models.receipt_dto import ReceiptDTO


class ReceiptEntity:
    def __init__(self, dto: ReceiptDTO):
        self.id = str(uuid4())
        self.retailer = dto.retailer
        self.purchase_date = dto.purchase_date
        self.purchase_time = dto.purchase_time
        self.item_list = dto.item_list
        self.total = dto.total
        self.points = 0  # Points will be calculated later
