import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_settings_route(client):
    response = client.get('/settings')
    assert response.status_code == 200
    assert b'Settings' in response.data

def test_dashboard_route(client):
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_monitoring_route(client):
    response = client.get('/monitoring')
    assert response.status_code == 200
    assert b'Monitoring' in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data
