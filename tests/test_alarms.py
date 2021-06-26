def test_get_alarms(client):
    assert client.get('/alarms').status_code == 200


def test_get_alarm(client):
    answer = client.get('/alarms/0')

    assert answer.status_code == 200

    json_data = answer.get_json()
    assert json_data['alarm']['hour'] == 10


def test_put_alarm(client):
    answer = client.put('/alarms/0', json={
        'id': '0',
        'hour': '10',
        'minute': '45',
        'days': '[1,2]',
        'enabled': 'True'})
    assert answer.status_code == 200


def test_delete_alarm(client):
    assert client.delete('/alarms/0').status_code == 200
