import os
from pathlib import Path
from environs import Env

env = Env()
env.read_env()


class Settings:
    SECRET_KEY = env.str("SECRET_KEY")

    PROJECT_ROOT = Path(__file__).parent.parent
    UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'media')

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 20 MB

    SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")

    FLASK_RUN_HOST = env.str("FLASK_RUN_HOST")
    FLASK_RUN_PORT = env.int("FLASK_RUN_PORT")
    FLASK_DEBUG = env.bool("FLASK_DEBUG")
