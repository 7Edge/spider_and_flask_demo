#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: manage
# Date: 5/6/2019

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from app import create_app
from app import db

app = create_app()
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
