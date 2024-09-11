# app/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    from app.auth import auth #importacion de los blue print
    from .routes import main
    app.register_blueprint(main)#registro de los blue print
    app.register_blueprint(auth)
    return app
