import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app



test_data = [
    [90, 90, 0, 0],
    [23, 90, 10, 693],
    [90, 90, 90, 90],
    [100, 90, 20, 50],
    [-20, 90, 10, 1080]
]


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    for test_case in test_data:
        response = client.post('/', data={'current_grade': test_case[0], 'percentage': test_case[1], 'weight': test_case[2]})
        assert response.status_code == 200
        assert bytes(str(test_case[3]), 'utf-8') in response.data
        print(response.data)

