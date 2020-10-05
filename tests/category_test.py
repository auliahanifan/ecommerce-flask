import json
from . import app, client, cache, create_token_admin_non_super

class TestClientCrud():
    var_id = 0

######### get list
    def test_category_get(self, client):
        token = create_token_admin_non_super()
        res = client.get('/api/category',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        
        assert res.status_code == 200

    def test_category_invalid_get(self, client):
        token = create_token_admin_non_super()
        res = client.get('/api/category2', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404
    
    def test_category_get_list(self, client):
        data = {
            "p": 1,
            "rp": 25,
            "id": 1,
            "orderby": "id",
            "sort": "asc"
            }
        res=client.get('/api/category', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200



######### get
    def test_category_get(self, client):
        token = create_token_admin_non_super()
        res = client.get('/api/category/1',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_category_invalid_get(self, client):
        token = create_token_admin_non_super()
        res = client.get('api/category/10000000', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_category_input(self, client):
        token = create_token_admin_non_super()
        data = {
        "name": "Kopi Susu",
        "description": "Kopi Susu"
        }
        res=client.post('/api/category', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['category_id']

        assert res.status_code == 200


    def test_category_invalid_input(self, client):
        token = create_token_admin_non_super()
        data = {
        "password": "123",
        "status": 0
        }
        res=client.post('/api/category', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### PUT

    def test_category_put(self, client):
        token = create_token_admin_non_super()
        data = {
        "name": "Kopi",
        "description": "Kopi"
        }
        res=client.put('/api/category/1', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_category_invalid_put(self, client):
        token = create_token_admin_non_super()
        data = {
        "name": "name"
        }
        res=client.put('/api/category/2', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400


######### delete
    def test_category_delete(self, client):
        token = create_token_admin_non_super()
        res=client.delete('api/category/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_category_invalid_delete(self, client):
        token = create_token_admin_non_super()
        res=client.delete('api/register/12', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 500

        