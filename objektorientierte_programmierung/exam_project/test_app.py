import unittest
from main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Breast Cancer Diagnosis', response.data)

    def test_generate(self):
        response = self.app.get('/generate')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generate Analysis', response.data)

    def test_results(self):
        response = self.app.get('/results')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Results', response.data)

if __name__ == '__main__':
    unittest.main()
