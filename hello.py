import sqlalchemy

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from config import *



postgres_uri = 'postgresql://{}:{}@{}:{}/{}'.format(
    POSTGRES['username'], POSTGRES['password'],
    POSTGRES['host'], POSTGRES['port'], POSTGRES['dbname'])

engine = create_engine(postgres_uri, encoding='utf-8', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

result = engine.execute('select * from user_login')

for row in result:
    print(row[0])


