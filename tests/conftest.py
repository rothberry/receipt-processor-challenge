import pytest
from app import create_app
from utils.read_json import read_json_file
from repositories.receipt_repository import ReceiptRepository
from services.receipt_service import ReceiptService
from models.receipt_dto import ReceiptDTO
from py_term_helpers import *


@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def repo():
    return ReceiptRepository()

@pytest.fixture
def service(repo):
    # repository = ReceiptRepository()
    return ReceiptService(repo)


@pytest.fixture
def sample_receipt():
    return ReceiptDTO(read_json_file("examples/test_bb.json"))


@pytest.fixture
def post_req_data():
    return read_json_file("examples/simple-receipt.json")


@pytest.fixture
def bad_post_req_data():
    return read_json_file("examples/bad-receipt.json")
