# -*- coding: utf-8 -*-
"""
Created on 2015-10-20 08:31:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

if DEBUG:
    FLASK_LOG_LEVEL = 'DEBUG'
else:
    FLASK_LOG_LEVEL = 'INFO'


POSTGRES = {
	'host': "172.17.42.1",
	'port': "5432",
	'username': "ofbiz",
	'password': "ofbiz",
	'dbname': "ofbiz"
}


DATABASE_BACKUP = 'olbius'
