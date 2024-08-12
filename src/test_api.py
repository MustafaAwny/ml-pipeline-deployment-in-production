import pytest
import pandas as pd
import numpy as np
from fastapi.testclient import TestClient
from .main import app


@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client


def test_get(client):
    
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome!"}


def test_inference_case1(client):
    r = client.post("/", json={
        "age": 16,
        "workclass": "Private",
        "education": "HS-grad",
        "maritalStatus": "Never-married",
        "occupation": "Other-service",
        "relationship": "Own-child",
        "race": "Black",
        "sex": "Male",
        "hoursPerWeek": 40,
        "nativeCountry": "United-States"
    })
    assert r.status_code == 200
    assert r.json() == {"prediction": "<=50K"}


def test_inference_case2(client):
    r = client.post("/", json={
        "age": 31,
        "workclass": "Private",
        "education": "Masters",
        "maritalStatus": "Never-married",
        "occupation": "Prof-speciality",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hoursPerWeek": 40,
        "nativeCountry": "United-States"
    })
    assert r.status_code == 200
    assert r.json() == {"prediction": ">50K"}




