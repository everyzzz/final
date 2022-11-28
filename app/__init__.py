from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config

from app.routes.rick_morty import rick_morty

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    Bootstrap(app)

    app.register_blueprint(rick_morty)
    
    return app