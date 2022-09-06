from flask_cors import CORS
from flask import Flask
from flasgger import Swagger
from api.config import create_db, create_tables, TestingConfig
from api.views import places_bp


def create_app() -> Flask:

    template = {
        "swagger": "2.0",
        "info": {
            "title": "Cities wishlist API",
            "description": "",
            "contact": {
                "responsibleOrganization": "",
                "responsibleDeveloper": "",
                "email": "",
                "url": "",
            },
            "termsOfService": "",
            "version": "0.2"
        },
        "basePath": "/",  # base bash for blueprint registration
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "getmyData"
    }

    swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'api',
                "route": '/api/docs/api.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/api/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/api/docs"
    }
    app = Flask(__name__)
    app.config.from_object(TestingConfig())
    CORS(app)
    app._db = create_db(app.config)
    create_tables(app._db)
    app._swagger = Swagger(app, template=template, config=swagger_config)
    app.register_blueprint(places_bp, url_prefix='/api')

    return app
