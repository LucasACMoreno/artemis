from flask_migrate import Migrate
from mysite.ext.db import db
from mysite.ext.db import models

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)