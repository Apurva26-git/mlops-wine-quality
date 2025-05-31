import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Iris Flower Predictor' in response.data  # Verifies HTML loads

def test_prediction(client):
    response = client.post('/predict', data={
        'sepal_length': 5.1,
        'sepal_width': 3.5,
        'petal_length': 1.4,
        'petal_width': 0.2
    })
    assert response.status_code == 200
    assert b'Prediction:' in response.data
    assert any(species in response.data for species in [
        b'Setosa', b'Versicolor', b'Virginica'
    ])