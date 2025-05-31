from flask import Flask
from src.config import Config
from src.ext import db, migrate
from src.view import product_blueprint, user_blueprint, main_blueprint
from src.commands import init_db, populate_db


Blueprints = [product_blueprint, user_blueprint, main_blueprint]
Commands = [init_db, populate_db]


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)


def register_blueprints(app):
    for blueprint in Blueprints:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in Commands:
        app.cli.add_command(command)


