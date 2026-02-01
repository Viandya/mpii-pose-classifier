from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_endpoint():
    files = {"image": ("test.jpg", b"fake_image_data", "image/jpeg")}
    response = client.post("/predict", files=files)
    assert response.status_code == 200
    assert "class" in response.json()
