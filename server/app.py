from flask import Flask, request, make_response
from py_term_helpers import top_wrap, center_string_stars
from ipdb import set_trace
from models import Receipt

app = Flask(__name__)

# In leiu of connecting flask to an actual database
# This list of 'receipt'
mock_database = []


@app.route("/")
def land():
    return "LANDED"


@app.route("/receipts/process", methods=["POST"])
def process_receipt():
    json_data = request.get_json()
    receipt = Receipt(json_data)
    # set_trace()
    # center_string_stars(receipt.id)
    return make_response({"id": receipt.id})


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


if __name__ == '__main__':
    PORT = 5555
    top_wrap(f"FLASK APP RUNNING ON PORT={PORT}")
    app.run(port=PORT, debug=False)
