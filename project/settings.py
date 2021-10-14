from environs import Env

env = Env()
env.read_env()


class Settings:
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
    FLASK_RUN_HOST = env.str("FLASK_RUN_HOST")
    FLASK_RUN_PORT = env.int("FLASK_RUN_PORT")
    FLASK_DEBUG = env.str("FLASK_DEBUG")
