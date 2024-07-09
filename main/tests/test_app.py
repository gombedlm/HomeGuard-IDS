import sys
import os

# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask import Flask
from app import app  # Adjust the import path as needed
from src.monitoring.monitoring import NetworkMonitor

# Create a test Flask application
@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    rv = client.get('/')
    assert b'HomeGuard IDS Dashboard' in rv.data

def test_monitoring(client):
    """Test the monitoring route."""
    rv = client.get('/monitoring')
    assert b'Monitor real-time network traffic and connectivity.' in rv.data

def test_settings(client):
    """Test the settings route."""
    rv = client.get('/settings')
    assert b'Settings' in rv.data

def test_dashboard(client):
    """Test the dashboard route."""
    rv = client.get('/dashboard')
    assert b'View system status and performance metrics.' in rv.data

def test_about(client):
    """Test the about route."""
    rv = client.get('/about')
    assert b'About HomeGuard IDS' in rv.data

def test_live_updates_data(client):
    """Test the live_updates_data route."""
    rv = client.get('/live_updates_data')
    assert rv.content_type == 'application/json'

def test_network_monitoring():
    """Test NetworkMonitor methods."""
    monitor = NetworkMonitor()
    all_interfaces, interfaces_with_internet, connected_wifi = monitor.monitor_networks()
    assert isinstance(all_interfaces, list)
    assert isinstance(interfaces_with_internet, list)
    assert isinstance(connected_wifi, list)

def test_anomaly_detection():
    """Test Detection class methods."""
    from src.detection.detection import Detection
    detector = Detection()

    # Test with mock data
    mock_data = [
        "Normal packet",
        "This is a malware packet",
        "Large packet exceeding MTU size",
        "AAA start packet"
    ]
    anomalies = detector.detect_anomalies(mock_data)
    assert len(anomalies) == 2  # Expecting 2 anomalies in mock data

# Entry point for running tests using pytest
if __name__ == '__main__':
    pytest.main()
