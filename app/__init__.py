# app/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_login import LoginManager
from .auth import auth # Importación de los blueprints
from .main import main
login_manger = LoginManager()
login_manger.login_view = 'auth.login'
def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    app.register_blueprint(main)  # Registro de blueprints
    app.register_blueprint(auth)
    return app
