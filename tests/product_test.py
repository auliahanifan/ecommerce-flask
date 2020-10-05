import json
from . import app, client, cache, create_token_admin_non_super

class TestClientCrud():
    var_id = 0

######### get list
    def test_product_get(self, client):
        # token = create_token_admin_non_super()
        res = client.get('/api/product/all')
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_get(self, client):

        res = client.get('/api/products')
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### get
    def test_product_get(self, client):

        res = client.get('/api/product/2')        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_get(self, client):
        res = client.get('/api/product/100')        
        res_json=json.loads(res.data)
        assert res.status_code == 404

# ######### post

    def test_product_input(self, client):
        token = create_token_admin_non_super()
        data = {
            "product_name": "Baju Baru",
            "product_stock": 50,
            "product_price": 18000,
            "product_weight": 300,
            "product_image_url": "https://images-na.ssl-images-amazon.com/images/I/4166cMJCseL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_PIStarRatingTWO%2CBottomLeft%2C360%2C-6_SR600%2C315_ZA(23%20Reviews)%2C445%2C291%2C400%2C400%2Carial%2C12%2C4%2C0%2C0%2C5_SCLZZZZZZZ_.jpg",
            "product_description": "Terbuat dari kopi pilihan dan rempah-rempah khas nusantara",
            "category_id": 1
        }
        res=client.post('/api/product', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        print(res_json)
        TestClientCrud.var_id = res_json['product_id']

        assert res.status_code == 200


    def test_product_invalid_input(self, client):
        token = create_token_admin_non_super()
        data = {
        "password": "123",
        "status": 0
        }
        res=client.post('/api/product', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

# ######### PUT

    def test_product_put(self, client):
        token = create_token_admin_non_super()
        data = {
            "product_name": "Baju Slim Sekali",
            "product_stock": 50,
            "product_price": 18000,
            "product_weight": 300,
            "product_image_url": "https://images-na.ssl-images-amazon.com/images/I/4166cMJCseL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_PIStarRatingTWO%2CBottomLeft%2C360%2C-6_SR600%2C315_ZA(23%20Reviews)%2C445%2C291%2C400%2C400%2Carial%2C12%2C4%2C0%2C0%2C5_SCLZZZZZZZ_.jpg",
            "product_description": "Terbuat dari kopi pilihan dan rempah-rempah khas nusantara",
            "category_id": 1
        }
        res=client.put('/api/product/5', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_product_invalid_put(self, client):
        token = create_token_admin_non_super()
        data = {
        "name": "name"
        }
        res=client.put('/api/product/2', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400


# ######### delete
    def test_product_delete(self, client):
        token = create_token_admin_non_super()
        res=client.delete('api/product/' + str(TestClientCrud.var_id), 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_product_invalid_delete(self, client):
        token = create_token_admin_non_super()
        res=client.delete('api/product21', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404


###### get all 

    def test_product_get_all(self, client):
        data = {
            "p": 1,
            "rp": 25,
            "id": 1,
            "orderby": "id",
            "sort": "asc"
            }
        res=client.get('/api/product/all', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200


    def test_product_get_all_by_category(self, client):
        data = {
            "p": 1,
            "rp": 25,
            "id": 1,
            "orderby": "id",
            "sort": "asc"
            }
        res=client.get('/api/product/category/1', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        assert res.status_code == 200

