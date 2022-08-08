from flask_cors import CORS
from flask import Flask, render_template, request
from peewee import fn
from shapely.geometry import shape
import json

from api.models import User, Place
from api.config import create_db, create_tables, TestingConfig


def create_app() -> Flask:

    app = Flask(__name__)
    app.config.from_object(TestingConfig())
    CORS(app)
    app.db = create_db(app.config)
    create_tables(app.db)

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/status')
    def status():
        if (point := Place.get_or_none(1)) is None:
            return {"message": "Error"}, 404
        else:
            return {"message": "Connected"}, 200
        # query = User.select()
        # if query.exists():
        #     return {'Message': "healthy"}, 200

    @app.route('/places', methods=['GET'])
    def get_place():
        places = Place.select(
            fn.ST_AsGeoJSON(Place.geom).alias('geom'),
            Place
        ).dicts()
        features = []
        for row in places:
            geom = row.pop('geom')
            features.append({
                "type": "Feature",
                "geometry": json.loads(geom),
                "properties": row
            })
        return {
            "type": "FeatureCollection",
            "features": features
        }

    @app.route('/places', methods=['POST'])
    def add_place():
        req = request.json
        geometry = 'SRID=4326;{}'.format(shape(req['geom']).wkt)
        Place.create(city=req['city'], country=req['country'],
                     notes=req['notes'], geom=geometry)
        return {"status": "added"}, 201

    @app.route('/places/<int:point_id>', methods=['DELETE'])
    def delete_place(point_id):
        if (point := Place.get_or_none(Place.id == point_id)) is None:
            return {"message": "Point not found"}, 404
        else:
            point.delete_instance()
            return {"message": "Point removed"}, 200

    return app
