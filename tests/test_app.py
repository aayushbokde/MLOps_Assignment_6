import json
from main import app

def test_predict_route():
    tester = app.test_client()
    response = tester.post(
        "/predict",
        data=json.dumps({"features": [5.1, 3.5, 1.4, 0.2]}),
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "prediction" in response.get_json()
