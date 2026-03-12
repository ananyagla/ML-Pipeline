import sys
sys.path.insert(0, '..')
from app import app

def test_health():
    client = app.test_client()
    res = client.get('/health')
    assert res.status_code == 200

def test_predict():
    client = app.test_client()
    res = client.post('/predict', json={"features": [0.9, 0.8, 0.9, 0.1]})
    assert res.status_code == 200