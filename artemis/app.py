from flask import Flask

from mysite.ext import site
from mysite.ext import db
from mysite.ext import config
from mysite.ext import cli
from mysite.ext import migrate
from mysite.ext import admin


def create_app():
    app = Flask(__name__)    
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
