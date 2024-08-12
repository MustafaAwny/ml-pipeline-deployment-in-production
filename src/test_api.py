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


def test_get_malformed(client):
    r = client.get("/oops")
    assert r.status_code != 200



def test_post_malformed(client):
    r = client.post("/", json={
        "age": 28,
        "workclass": "Private",
        "education": " Bachelors",
        "maritalStatus": " Married-civ-spouse",
        "occupation": " Prof-specialty",
        "relationship": " Wife",
        "race": "Black",
        "sex": "Female",
        "hoursPerWeek": 40,
        "nativeCountry": "Cuba"
    })
    assert r.status_code != 200