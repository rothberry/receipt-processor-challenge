from flask import Flask, request, make_response
from py_term_helpers import top_wrap, center_string_stars
from ipdb import set_trace
from server.models import Receipt
import json


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def land():
        return "LANDED"

    @app.route("/receipts/process", methods=["POST"])
    def process_receipt():
        json_data = request.get_json()
        try:
            receipt = Receipt(json_data)
            return make_response({"id": receipt.id})
        except:
            return make_response({"error": "Failed to create receipt"}, 400)

    @app.route("/receipts/<string:receipt_id>/points")
    def get_points(receipt_id):
        center_string_stars(receipt_id)
        found_receipt = None
        for r in Receipt.all:
            if r.id == receipt_id:
                found_receipt = r
        if found_receipt:
            return make_response({"points": found_receipt.points})
        else:
            return make_response({"error": f"Receipt of id {receipt_id} not found"}, 404)

    @app.route("/receipts")
    def all_receipts():
        receipts = Receipt.all
        json_receipts = [{"id": r.id, "points": r.points} for r in receipts]
        return make_response(json_receipts)

    return app


if __name__ == '__main__':
    from server.helpers import create_receipt_from_file
    PORT = 5555
    top_wrap(f"FLASK APP RUNNING ON PORT={PORT}")

    center_string_stars("CREATING SEED DATA FROM EXAMPLES")
    create_receipt_from_file("examples/morning-receipt.json")
    create_receipt_from_file("examples/simple-receipt.json")
    app = create_app()
    app.run(port=PORT, debug=False)
