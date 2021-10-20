from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_file_upload import FileUpload

from project.settings import Settings

migrate = Migrate()
app = Flask(__name__)
app.config.from_object(Settings)
db = SQLAlchemy(app)
migrate.init_app(app=app, db=db)
ma = Marshmallow(app)
file_upload = FileUpload(app, db)

from app.models import users
from app.models import blog
from app import routes
