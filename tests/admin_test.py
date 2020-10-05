import json
from . import app, client, cache, create_token_admin_super, create_token_admin_non_super

class TestClientCrud():
    var_id = 0

######### get list
    def test_admin_list(self, client):
        token = create_token_admin_super()
        res = client.get('/api/admin',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_admin_invalid_list(self, client):
        token = create_token_admin_super()
        res = client.get('/api/admin2', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### get
    def test_admin_get(self, client):
        token = create_token_admin_super()
        res = client.get('/api/admin/1',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_admin_invalid_get(self, client):
        token = create_token_admin_super()
        res = client.get('api/admin/100', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_admin_input(self, client):
        token = create_token_admin_super()
        data = {
        "username": "admin233",
        "password": "123",
        "status": 0 
        }
        res=client.post('/api/admin', 
                        data=json.dumps(data),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['admin_id']

        assert res.status_code == 200


    def test_admin_invalid_input(self, client):
        token = create_token_admin_super()
        data = {
        "password": "123",
        "status": 0
        }
        res=client.post('/api/admin', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 500

######### PUT

    def test_admin_put(self, client):
        token = create_token_admin_super()
        data = {
        "username": "admin233",
        "password": "123",
        "status": 0
        }
        res=client.put('/api/admin/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_admin_invalid_put(self, client):
        token = create_token_admin_super()
        data = {
        "per_page": 1,
        "keywords":"AUL"
        }
        res=client.put('/api/admin/1000', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400


######### delete
    def test_admin_delete(self, client):
        token = create_token_admin_super()
        res=client.delete('api/admin/' +str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_admin_invalid_delete(self, client):
        token = create_token_admin_super()
        res=client.delete('api/admin/2', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        