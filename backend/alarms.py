from flask import Blueprint, request, jsonify
import uuid

ALARMS = [
    {
        'id': uuid.uuid4().hex,
        'days': '0',
        'hour': 7,
        'minutes': 30,
        'enabled': True
    },
    {
        'id': uuid.uuid4().hex,
        'days': '5, 6',
        'hour': 10,
        'minutes': 0,
        'enabled': False
    },
    {
        'id': uuid.uuid4().hex,
        'days': '1, 2',
        'hour': 7,
        'minutes': 0,
        'enabled': True
    }
]

alarms_bp = Blueprint('alarms_bp', __name__)


# alarms route
@alarms_bp.route('', methods=['GET', 'POST'])
def all_alarms():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        ALARMS.append({
            'id': uuid.uuid4().hex,
            'days': post_data.get('days'),
            'hour': post_data.get('hour'),
            'minutes': post_data.get('minutes'),
            'enabled': True
        })
        response_object['message'] = 'Alarm added!'
    else:
        response_object['alarms'] = ALARMS

    return jsonify(response_object)


# alarm route
@alarms_bp.route('/<alarm_id>', methods=['PUT', 'DELETE'])
def single_alarm(alarm_id):
    response_object = {'status': 'success'}

    if request.method == 'DELETE':
        remove_alarm(alarm_id)
    elif request.method == 'PUT':
        post_data = request.get_json()
        remove_alarm(alarm_id)
        ALARMS.append({
            'id': uuid.uuid4().hex,
            'hour': post_data.get('hour'),
            'minutes': post_data.get('minutes'),
            'enabled': True,
            'days': post_data.get('days')
        })
        response_object['message'] = 'Alarm updated!'

    return jsonify(response_object)


def remove_alarm(id):
    for alarm in ALARMS:
        if alarm['id'] == id:
            ALARMS.remove(alarm)
            return True
    return False
