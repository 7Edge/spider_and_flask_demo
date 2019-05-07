#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: __init__.py
# Date: 5/6/2019

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .views import crawler
from .views import normal
from .models import *

def create_app():
    app = Flask(import_name=__name__)
    app.config.from_object('settings.DevConfig')

    app.register_blueprint(blueprint=crawler.crawler_bp)
    app.register_blueprint(blueprint=normal.normal_bp)

    db.init_app(app)

    return app


if __name__ == '__main__':
    pass
