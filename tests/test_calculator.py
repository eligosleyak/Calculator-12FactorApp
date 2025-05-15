"""
Test suite for the Calculator API endpoints.
This module contains tests for all arithmetic operations provided by the API.
"""

from fastapi.testclient import TestClient
from app.main import app

# Create a test client instance
client = TestClient(app)


def test_welcome():
    """
    Test the welcome endpoint returns the correct greeting message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the CalculatorAPI"}


def test_add():
    """
    Test the addition endpoint with positive integers.
    Tests if 5 + 3 equals 8.
    """
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_subtract():
    """
    Test the subtraction endpoint with positive integers.
    Tests if 10 - 4 equals 6.
    """
    response = client.get("/subtract/10/4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_multiply():
    """
    Test the multiplication endpoint with positive integers.
    Tests if 6 * 7 equals 42.
    """
    response = client.get("/multiply/6/7")
    assert response.status_code == 200
    assert response.json() == {"result": 42}


def test_divide():
    """
    Test the division endpoint with positive integers.
    Tests if 20 / 5 equals 4.0.
    """
    response = client.get("/divide/20/5")
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}
