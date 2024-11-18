import os


class Settings:
    STATIC_FOLDER: str = '../static'
    TEMPLATE_FOLDER: str = '../templates'

    SECRET_KEY: str = os.getenv("TOKEN_SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")