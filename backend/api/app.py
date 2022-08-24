from flask_cors import CORS
from flask import Flask
from flasgger import Swagger

from api.config import create_db, create_tables, TestingConfig
from api.views import places_bp


def create_app() -> Flask:

    app = Flask(__name__)
    app.config.from_object(TestingConfig())
    CORS(app)
    app._db = create_db(app.config)
    create_tables(app._db)
    app._swagger = Swagger(app)
    app.register_blueprint(places_bp)

    return app
