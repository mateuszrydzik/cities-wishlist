import os
from api.models import database, User, Place


class Config(object):
    TESTING = False
    DBNAME = os.environ.get('POSTGRES_DBNAME')
    DBHOST = os.environ.get('CONTAINER_NAME') + '_db'
    DBUSER = os.environ.get('POSTGRES_USER')
    DBPASS = os.environ.get('POSTGRES_PASSWORD')
    DBPORT = os.environ.get('DB_PORT')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class TestingConfig(Config):
    TESITNG = True


def create_db(config):
    database.init(
        config['DBNAME'],
        host=config['DBHOST'],
        user=config['DBUSER'],
        password=config['DBPASS'],
        port=config['DBPORT']
    )
    return


models = [User, Place]


def create_tables(database):
    for model in models:
        model.create_table()
