from models.receipt_entity import ReceiptEntity
from services.points_calculator import PointsCalculator

class ReceiptService:
    def __init__(self, repository):
        self.repository = repository

    def create_receipt(self, receipt_dto):
        receipt = ReceiptEntity(receipt_dto)
        receipt.points = PointsCalculator.calculate(receipt)
        self.repository.save(receipt)
        return receipt

    def get_receipt_by_id(self, receipt_id):
        return self.repository.get_by_id(receipt_id)