from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the CalculatorAPI"}


def test_add():
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_subtract():
    response = client.get("/subtract/10/4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_multiply():
    response = client.get("/multiply/6/7")
    assert response.status_code == 200
    assert response.json() == {"result": 42}


def test_divide():
    response = client.get("/divide/20/5")
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}
