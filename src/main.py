from typing import Type
from flask import Flask, render_template

from app import auth_bp, food_bp
from app.auth import auth

from db import db, migrate
from config import Settings


def create_app(config: Type[Settings] = Settings):
    app = Flask(__name__)

    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(food_bp)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app)
        auth.init_app(app)

    return app