from models import database, User, Place


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
        model.create_table
