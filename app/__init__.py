# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
bcrypt = Bcrypt()


def create_app(config_type):  # config_type can be dev, test, or prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
# yields C:\\Python2\\book_catalog\\config\\dev.py
    app.config.from_pyfile(configuration)

    db.init_app(app)  # bind database to flask app
    bootstrap.init_app(app) # init bootstrap - bind to app
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main  # import Blueprint
    app.register_blueprint(main)  # register Blueprint

    from app.auth import authentication
    app.register_blueprint(authentication)
    app.config['SECRET_KEY'] = 'secret'
    return app
