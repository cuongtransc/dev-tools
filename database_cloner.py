# -*- coding: utf-8 -*-
"""
Created on 2015-10-20 08:43:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""
import logging
import sys
import datetime

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import POSTGRES

logger = logging.getLogger('database_cloner')
logging.basicConfig(stream=sys.stderr, level=getattr(logging, 'INFO'))


class DatabaseCloner():
    def __int__(self):
        pass

    def connect(self):
        con = psycopg2.connect(database=POSTGRES['dbname'],
                               user=POSTGRES['username'],
                               password=POSTGRES['password'],
                               host=POSTGRES['host'],
                               port=POSTGRES['port']
                               )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return con

    def create_db(self, db_name, owner):
        """
        Create database postgres
        :param db_name:
        :param owner:
        :return:
        """
        con = self.connect()
        cur = con.cursor()

        cur.execute('''
            CREATE DATABASE %s WITH ENCODING='UTF8' OWNER=%s;
        ''' % (db_name, owner)
                    )
        con.commit()
        con.close()

    def clone_db(self, db_source, db_dest, owner, is_force=False, is_terminate=False):
        """
        Clone database from template
        :param db_tmpl:
        :param db_dest:
        :param owner:
        :param is_force: overwrite db_dest
        :return:
        """
        con = self.connect()
        cur = con.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = '%s'" % (db_dest))

        if cur.fetchone():
            if not is_force:
                # do nothing
                logging.info('nothing')
                return
            else:  # if is_force: drop database
                # stop all connect to database
                cur.execute('''
                    SELECT pg_terminate_backend(pg_stat_activity.pid)
                    FROM pg_stat_activity
                    WHERE pg_stat_activity.datname = '%s'
                      AND pid <> pg_backend_pid();
                ''' % (db_dest))

                # drop old database
                cur.execute('''
                    DROP DATABASE %s;
                ''' % (db_dest))

        if is_terminate:
            # stop all connect to database
            cur.execute('''
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = '%s'
                  AND pid <> pg_backend_pid();
            ''' % (db_source))

        # clone new database from template
        cur.execute('''
            CREATE DATABASE %s WITH TEMPLATE %s OWNER %s;
        ''' % (db_dest, db_source, owner))

        con.commit()
        con.close()

    def get_list_schemas(self, pattern=''):
        con = self.connect()
        cur = con.cursor()

        if not pattern:
            query = '''
                SELECT datname
                FROM pg_database
                WHERE datistemplate=false;
            '''
        else:
            query = '''
                SELECT datname
                FROM pg_database
                WHERE datistemplate=false
                    AND datname like '{}%';
            '''.format(pattern)

        cur.execute(query)
        result = cur.fetchall()
        schemas = [t[0] for t in result]

        return schemas

    def backup(self, db_source, db_dest=''):
        if not db_dest:
            timenow = datetime.datetime.now()
            db_dest = '{}_{}'.format(db_source, timenow.strftime('%Y%m%d_%H%M%S'))

        logger.info('backup: {} to {} ...'.format(db_source, db_dest))
        self.clone_db(db_source, db_dest, 'ofbiz', True, True)
        logger.info('backup: done!')
        return db_dest

    def restore(self, db_source, db_dest):
        logger.info('restore: {} to {} ...'.format(db_source, db_dest))
        self.clone_db(db_source, db_dest, 'ofbiz', True, True)
        logger.info('restore: done!')


def main():
    database_cloner = DatabaseCloner()
    # database_cloner.clone_db('dms_olbius', 'dms_olbius_20151021', 'ofbiz', is_force=True, is_terminate=True)

    # database_cloner.backup('dms_olbius')
    # database_cloner.restore('dms_olbius_20151020_153310', 'dms_olbius')
    pattern = 'dms_olbius_'

    # print(database_cloner.get_list_schemas())
    print(database_cloner.get_list_schemas(pattern))


if __name__ == '__main__':
    main()
