import pytest
from ipdb import set_trace
from app import create_app
from server.helpers import create_receipt_from_file


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
    create_receipt_from_file("examples/morning-receipt.json")
    create_receipt_from_file("examples/simple-receipt.json")
    return True