from flask_cors import CORS
from flask import Flask
from flasgger import Swagger
from api.config import create_db, create_tables, TestingConfig
from api.views import places_bp


def create_app() -> Flask:

    template = {
        "swagger": "2.0",
        "info": {
            "title": "My API",
            "description": "API for my data",
            "contact": {
                "responsibleOrganization": "ME",
                "responsibleDeveloper": "Me",
                "email": "me@me.com",
                "url": "www.me.com",
            },
            "termsOfService": "http://me.com/terms",
            "version": "0.0.1"
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
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    app = Flask(__name__)
    app.config.from_object(TestingConfig())
    CORS(app)
    app._db = create_db(app.config)
    create_tables(app._db)
    app._swagger = Swagger(app, template=template, config=swagger_config)
    app.register_blueprint(places_bp)

    return app
