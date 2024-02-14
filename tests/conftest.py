import pytest
from app import create_app
from server.helpers import create_receipt_from_file, read_json_file


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
def seed_data():
    create_receipt_from_file("examples/test_target.json")
    create_receipt_from_file("examples/test_corner.json")
    return True

@pytest.fixture
def post_req_data():
    return read_json_file("examples/simple-receipt.json")

@pytest.fixture
def bad_post_req_data():
    return read_json_file("examples/bad-receipt.json")
