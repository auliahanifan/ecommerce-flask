import json
from . import app, client, cache, create_token_user_available

class TestClientCrud():
    var_id = 0

    def test_user_get_all(self, client):
        token = create_token_user_available()
        res = client.get('/api/transaction_details',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_user_get_one(self, client):
        token = create_token_user_available()
        res = client.get('/api/transaction_details/1',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200
