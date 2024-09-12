from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from app.auth import auth
from .routes import main

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    
    app.register_blueprint(main)  # Registro del blueprint 'main'
    app.register_blueprint(auth)  # Registro del blueprint 'auth'
    
    return app