import pytest
from flask import Flask

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    # Add other configurations as needed
    yield app

def test_app_exists(app):
    assert app

def test_app_is_testing(app):
    assert app.config['TESTING']
