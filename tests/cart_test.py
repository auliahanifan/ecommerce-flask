import json
from . import app, client, cache, create_token_user, create_token_user_available

class TestClientCrud():
    var_id = 0

######### get list
    def test_cart_get(self, client):
        token = create_token_user_available()
        res = client.get('/api/cart',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_cart_invalid(self, client):
        token = create_token_user_available()
        res = client.get('/api/cart2', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404


# ######### post

    def test_cart_input(self, client):
        token = create_token_user_available()
        data = {
            "product_id": 1,
            "qty": 1
        }
        res=client.post('/api/cart', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['cart_id']

        assert res.status_code == 200

    def test_cart_input_over(self, client):
        token = create_token_user_available()
        data = {
            "product_id": 1,
            "qty": 1000000
        }
        res=client.post('/api/cart', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200



    def test_cart_invalid_input(self, client):
        token = create_token_user_available()
        data = {
        "password": "user",
        "status": 0
        }
        res=client.post('/api/cart', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

# ######### PUT

    def test_cart_put(self, client):
        token = create_token_user_available()
        data = {
            "product_id": 1,
            "qty": 1
        }
        res=client.put('/api/cart/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_cart_put_over(self, client):
        token = create_token_user_available()
        data = {
            "product_id": 2,
            "qty": 10000
        }
        res=client.put('/api/cart/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_cart_invalid_put(self, client):
        token = create_token_user_available()
        data = {
        "per_page": 1,
        "keywords":"AUL"
        }
        res=client.put('/api/cart', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 500


# ######### delete
    def test_cart_delete(self, client):
        token = create_token_user_available()
        res=client.delete('api/cart/'+ str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_cart_delete_invalid(self, client):
        token = create_token_user_available()
        res=client.delete('api/carts/'+ str(str(TestClientCrud.var_id)), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        