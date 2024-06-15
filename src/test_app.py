import pytest
from fastapi.testclient import TestClient
from app_solution import app


@pytest.fixture
def client():
    return TestClient(app)


def test_predict(client: TestClient):
    r = client.post("/predict", json={"passwords": ["qwerty123", "321ytrewq"]})
    assert r.status_code == 200
