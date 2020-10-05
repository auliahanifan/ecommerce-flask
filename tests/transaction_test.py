import json
from . import app, client, cache, create_token_admin_non_super, create_token_user, create_token_user_available

class TestClientCrud():
    var_id = 0

    def test_cart_input(self, client):
        token = create_token_user_available()
        data = {
            "product_id": 3,
            "qty": 1
        }
        res=client.post('/api/cart', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_transaction_input(self, client):
        token = create_token_user_available()
        data = {
            "full_name": "katrok",
            "handphone": "085726262626",
            "address": "jln. a no.2",
            "province": "jawa tengah",
            "city": "purwokerto",
            "district": "pwt timurr",
            "zip_code": "53161",
            "note": ""
        }
        res=client.post('/api/transaction', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['transaction_id']


        assert res.status_code == 200


    def test_user_get(self, client):
        token = create_token_user_available()
        res = client.get('/api/transaction',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200


    def test_trx_put(self, client):
        token = create_token_admin_non_super()
        data = {
            "status": 10
        }
        res=client.put('/api/transaction/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_admin_trx_get(self, client):
        token = create_token_admin_non_super()
        data = {
            "p": 1,
            "rp": 5
        }
        res=client.get('/api/transaction/all', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

