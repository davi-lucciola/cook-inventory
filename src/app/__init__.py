from .auth.auth_controller import auth_bp
from .category.category_controller import category_bp
from .inventory.inventory_controller import inventory_bp

from typing import Type
from flask import Flask

from app import auth_bp, inventory_bp
from app.auth import login_manager

from db import db, migrate
from config import Settings


def create_app(config: Type[Settings] = Settings):
    app = Flask(
        __name__, 
        static_folder=config.STATIC_FOLDER, 
        template_folder=config.TEMPLATE_FOLDER
    )

    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(inventory_bp)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app)
        login_manager.init_app(app)

    return app
