from fastapi.testclient import TestClient
from main import app  # Importing your 'app' object from main.py

client = TestClient(app)

def test_read_root():
    response = client.get("/hello-world")
    assert response.status_code == 200
    # Checks if the response matches what we expect
    assert response.json() == {"message": "Hello world"}