from flask import Flask
from yedioapp.config import config



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')

    from yedioapp.main.views import main

    app.register_blueprint(main)

    return app
