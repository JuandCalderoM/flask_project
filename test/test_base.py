from flask_testing import TestCase
from flask import current_app, url_for
from main import main as app
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
    #aqui verifico si se  logro un get
    def test_coment_get(self):
        response=self.client.get(url_for('contactanos_view'))
        self.assert200(response)
    #aqui se aprobueba un post
    def test_commet_post(self):
        fake_form = {
            'Nombre': 'fake',
            'Correo Electronico': 'fake@fake.com',
            'Tema':'prueba test',
            'commentario':'lorem moment fake'

        }
        response = self.client.post(url_for('contactanos_view'), data=fake_form)
        self.assert200(response)
