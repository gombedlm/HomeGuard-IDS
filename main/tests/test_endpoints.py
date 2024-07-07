import os
import sys
import unittest

# Insert the parent directory into sys.path to import app from main/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main.app import app  # Assuming app.py is in main/

class TestAppEndpoints(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to HomeGuard IDS Dashboard', response.data)

    def test_login_endpoint(self):
        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ))
        self.assertEqual(response.status_code, 404)  # Adjust this as per your application's actual behavior

if __name__ == '__main__':
    unittest.main()
