# -*- coding: utf-8 -*-
"""
Created on 2015-10-20 08:31:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

APP_HOST = '0.0.0.0'
APP_PORT = 5000

DEBUG = True

if DEBUG:
    FLASK_LOG_LEVEL = 'DEBUG'
else:
    FLASK_LOG_LEVEL = 'INFO'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

POSTGRES = {
    'host': "172.17.42.1",
    'port': "5432",
    'username': "coclab",
    'password': "coclab@123",
    'dbname': "coclab"
}

DATABASE_BACKUP = 'ofbiz'
