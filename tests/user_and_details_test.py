import json
from . import app, client, cache, create_token_admin_super, create_token_user, create_token_user_available

class TestClientCrud():
    var_id = 0

######### get list
    def test_user_get(self, client):
        token = create_token_user_available()
        res = client.get('/api/register',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_user_invalid(self, client):
        token = create_token_user_available()
        res = client.get('/api/register2', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404


######### post

    def test_user_input(self, client):
        
        data = {
        "username": "user15",
        "email": "123@gmail.com",
        "password": "123" 
        }
        res=client.post('/api/register', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['user_id']

        assert res.status_code == 200


    def test_user_invalid_input(self, client):
        # token = create_token_admin_super()
        data = {
        "password": "123",
        "status": 0
        }
        res=client.post('/api/register', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400
############## get user details 404
    def test_user_details_invalid(self, client):
        token = create_token_user()
        res = client.get('/api/user_details', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404


############# userdetails post
    def test_user_details_input(self, client):
        token = create_token_user()
        data = {
            "full_name": "Aulia",
            "address": "Jalan Tidar",
            "sex": "m",
            "phone": "085726317318",
            "province": "Jawa Timur",
            "city": "Malang",
            "district": "Sukun",
            "zip_code": "53161"
        }
        res=client.post('/api/user_details',
                        headers={'Authorization': 'Bearer ' + token}, 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        assert res.status_code == 200


######## get userdetails
    def test_user_details_get(self, client):
        token = create_token_user()
        res = client.get('/api/user_details',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200



######### PUT

    def test_user_put(self, client):
        token = create_token_user()
        data = {
        "username": "user15",
        "email": "auliarahman@gmail.com",
        "password": "123"
        }
        res=client.put('/api/register', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_user_invalid_put(self, client):
        token = create_token_user()
        data = {
        "per_page": 1,
        "keywords":"AUL"
        }
        res=client.put('/api/register', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

############################ user details put

    def test_user_details_put_succed(self, client):
        token = create_token_user()
        data = {
            "full_name": "Aulia",
            "address": "Jalan Tidar",
            "sex": "m",
            "phone": "085726317318",
            "province": "Jawa Timur",
            "city": "Malang",
            "district": "Sukun",
            "zip_code": "53161"
        }
        res=client.put('/api/user_details',
                        headers={'Authorization': 'Bearer ' + token}, 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['user_id']

        assert res.status_code == 200

#########user details delete
    def test_user_details_delete(self, client):
        token = create_token_user()
        res=client.delete('api/user_details', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200



######### delete
    def test_user_delete(self, client):
        token = create_token_user()
        res=client.delete('api/register', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_user_invalid_delete(self, client):
        token = create_token_user()
        res=client.delete('api/register/12', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 500

        