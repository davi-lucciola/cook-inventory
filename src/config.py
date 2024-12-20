import os
import dotenv as env


env.load_dotenv()


class Settings:
    BUCKET = 'cook-inventory-imgs'
    STATIC_FOLDER: str = '../static'
    TEMPLATE_FOLDER: str = '../templates'

    SECRET_KEY: str = os.getenv("TOKEN_SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")