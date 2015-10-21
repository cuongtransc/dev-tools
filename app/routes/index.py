# -*- coding: utf-8 -*-

from app import app
from flask import jsonify, request

from database_cloner import DatabaseCloner
from config import DATABASE_BACKUP


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/api/db/backup', methods=['POST'])
def backup_database():
    db_cloner = DatabaseCloner()
    snapshotId = db_cloner.backup(DATABASE_BACKUP)

    msg = dict()
    msg['status'] = 'success'
    msg['snapshotId'] = snapshotId

    return jsonify(msg)


@app.route('/api/db/restore', methods=['POST'])
def restore_database():
    snapshotId = request.json['snapshotId']
    app.logger.info('restore: snapshotId = {}'.format(snapshotId))

    db_cloner = DatabaseCloner()
    db_cloner.restore(snapshotId, DATABASE_BACKUP)

    msg = dict()
    msg['status'] = 'success'

    return jsonify(msg)


@app.route('/api/db/snapshots', methods=['GET'])
def get_snapshots():
    db_cloner = DatabaseCloner()
    snapshot_pattern = '{}\_'.format(DATABASE_BACKUP)
    snapshots = db_cloner.get_list_schemas(snapshot_pattern)

    msg = dict()
    msg['status'] = 'success'
    msg['snapshots'] = sorted(snapshots, reverse=True)

    return jsonify(msg)
