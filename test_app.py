from app import app
import json

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Iris Prediction API is running" in response.data

def test_prediction():
    response = app.test_client().post('/predict', 
        data=json.dumps({'features': [5.1, 3.5, 1.4, 0.2]}),
        content_type='application/json')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'prediction' in json_data
    assert json_data['prediction'] in [0, 1, 2]
