from backend.db import get_db, query_db
from flask import Blueprint, request, jsonify, abort
import uuid

alarms_bp = Blueprint('alarms_bp', __name__)


# alarms route
@alarms_bp.route('', methods=['GET', 'POST'])
def all_alarms():
    response_object = {'status': 'success'}

    db = get_db()
    if request.method == 'POST':
        post_data = request.get_json()
        db.execute('INSERT INTO alarm (id, days, hour, minute, enabled) \
                    VALUES (?, ?, ?, ?, ?)',
                   (uuid.uuid4().hex,
                    post_data.get('days'),
                    post_data.get('hour'),
                    post_data.get('minute'),
                    True)
                   )
        db.commit()
        response_object['message'] = 'Alarm added!'
    else:
        alarms = query_db('SELECT * FROM alarm')
        response_object['alarms'] = [dict(alarm) for alarm in alarms]

    return jsonify(response_object)


# alarm route
@alarms_bp.route('/<alarm_id>', methods=['GET', 'PUT', 'DELETE'])
def single_alarm(alarm_id):
    response_object = {'status': 'success'}

    db = get_db()

    if request.method == 'GET':
        alarm = query_db('SELECT * FROM alarm WHERE id = ?', (alarm_id), True)
        if alarm is None:
            abort(404)
        response_object['alarm'] = dict(alarm)
    elif request.method == 'DELETE':
        db.execute('DELETE FROM alarm WHERE id = ?', (alarm_id))
        db.commit()
        response_object['message'] = 'Alarm delete!'
    elif request.method == 'PUT':
        put_data = request.get_json()
        sql = ''' UPDATE alarm
                  SET hour = ?,
                      minute = ?,
                      enabled = ?,
                      days = ?
                  WHERE id = ? '''
        db.execute(sql, (put_data.get('hour'),
                         put_data.get('minute'),
                         True,
                         put_data.get('days'),
                         alarm_id))
        db.commit()
        response_object['message'] = 'Alarm updated!'

    return jsonify(response_object)
