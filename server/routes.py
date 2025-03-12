from flask import Blueprint, make_response, request
from repositories.receipt_repository import ReceiptRepository
from services.receipt_service import ReceiptService
from models.receipt_dto import ReceiptDTO
from ipdb import set_trace
from py_term_helpers import *

flask_app = Blueprint('flask_app', __name__)
repo = ReceiptRepository()
service = ReceiptService(repo)


# * Defining Routes
@flask_app.route("/")
def land():
    return "LANDED"

# ==========


@flask_app.route("/receipts/process", methods=["POST"])
def create_receipt():
    try:
        data = request.json
        center_string_stars(f"CREATING RECEIPT")
        receipt_dto = ReceiptDTO(data)
        receipt = service.create_receipt(receipt_dto)
        return make_response({"id": receipt.id}), 201
    except ValueError as e:
        return make_response({"error": str(e)}), 400


@flask_app.route("/receipts/<string:receipt_id>/points")
def get_receipt(receipt_id):
    center_string_stars(f"GETTING RECEIPT id: {receipt_id}")
    receipt = service.get_receipt_by_id(receipt_id)
    if receipt:
        return make_response({"points": receipt.points})
    return make_response({"error": "Receipt not found"}), 404

# ==========
