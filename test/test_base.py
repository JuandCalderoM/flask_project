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
    def test_auth_blueprint_exists(self): #existe el blueprint de auth
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)
    def test_auth_login_template(self): #verifica la existencia de mi tempalte login
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')
    def test_auth_login_post(self):
        fake_form = {
        'username': 'fake',
        'password': 'fake-password'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('auth.session_page'))

    