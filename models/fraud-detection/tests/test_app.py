import pytest, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_predict(client):
    res = client.post("/predict", json={"features": [0.5, 0.5, 0.5]})
    assert res.status_code == 200

def test_predict_missing(client):
    res = client.post("/predict", json={})
    assert res.status_code == 400