import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to HomeGuard' in response.data

# Add more endpoint tests as needed
