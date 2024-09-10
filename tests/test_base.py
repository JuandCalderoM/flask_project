from flask_testing import TestCase
from flask import current_app, url_for
from app import app
class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    #Aqui verifico la existencia del app
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    #Aqui verifico el estado del app
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    #aqui verifico la redirecion de un metodo a oto
    def test_inicio_redirect(self):
        response=self.client.get(url_for('index'))
        self.assertRedirects(response,url_for('blog'))
    #aqui verifico si se aprobo el post
    def test_inicio_redirect(self):
        response=self.client.get(url_for('contactanos_view'))
        self.assert200(response)