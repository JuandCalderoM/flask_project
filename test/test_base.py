from flask_testing import TestCase
from flask import current_app, url_for
from main import create_app  # Asegúrate de importar tu función de creación de app

class MainTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_coment_get(self):
        response = self.client.get('/contactanos')
        self.assert200(response)

    def test_commet_post(self):
        fake_form = {
            'name': 'fake',
            'email': 'fake@fake.com',
            'subject': 'prueba test',
            'comments': 'lorem moment fake'
        }
        response = self.client.post('/contactanos', data=fake_form, follow_redirects=True)
        self.assert200(response)
