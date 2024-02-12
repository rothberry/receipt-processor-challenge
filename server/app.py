from flask import Flask, request
from py_term_helpers import top_wrap
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
    set_trace()


if __name__ == '__main__':
    PORT = 5555
    top_wrap(f"FLASK APP RUNNING ON PORT={PORT}")
    app.run(port=PORT, debug=False)
