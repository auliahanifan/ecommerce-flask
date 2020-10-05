# Ecommerce Flask

This is prototype of Ecommerce with Flask.

___

## Requirements

1. Python 3.7+
2. MySQL

___

## Operations

### Configs

All configs is stored in `.env` file, please create your own `.env` file, the example is in `.env-sample` file.

Note:
There is 2 database: for production and testing. Please fill it.
If environment variable `TESTING=True`, database used is for testing.

### Testing
You can test this code:
1. Activate VirtualEnv first.
2. `pip install -r requirements.txt`
3. Set environment variable `TESTING=True` (you can use .env)
4. Make sure you have migrate, `python app.py db migrate`
5. Make sure your db is filled, you can seed it by `python app.py seed`
6. `pytest --cov-report html --cov=blueprints tests`

### Run
You can run this app by:
1. Activate VirtualEnv.
2. `pip install -r requirements.txt`
3. Make sure all `.env` have been filled truly
4. Make sure you have migrate, `python app.py db migrate`
5. `python app.py`