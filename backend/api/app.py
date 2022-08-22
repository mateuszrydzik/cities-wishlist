from operator import truediv
from flask_cors import CORS
from flask import Flask, render_template, request
from peewee import fn
from shapely.geometry import shape
import json

from api.models import Place
from api.config import create_db, create_tables, TestingConfig


def create_app() -> Flask:

    app = Flask(__name__)
    app.config.from_object(TestingConfig())
    CORS(app)
    app.db = create_db(app.config)
    create_tables(app.db)

    @app.route('/status')
    def status():
        if (Place.get_or_none()) is None:
            return {"message": "Not connected"}, 404
        else:
            return {"message": "Connected"}, 200

    @app.route('/places', methods=['GET'])
    def get_places():
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

    @app.route('/places/<int:place_id>', methods=['GET'])
    def get_place(place_id):
        if (Place.get_or_none(Place.id == place_id)) is None:
            return {"message": "Place not found"}, 404
        else:
            one = Place.select(fn.ST_AsGeoJSON(Place.geom).alias('geom'), Place
                               ).where(Place.id == place_id).dicts().get()

            return {"type": "Feature",
                    "geometry": json.loads(one.pop('geom')),
                    "properties": one}, 200

    @app.route('/places/<int:place_id>', methods=['PUT'])
    def update_place(place_id):
        if (place := Place.get_or_none(Place.id == place_id)) is None:
            return {"message": "Place not found"}, 404
        else:
            place.notes = request.args.get('notes')
            place.save()
            return {"message": "Place updated"}, 204

    @app.route('/places/<int:place_id>', methods=['DELETE'])
    def delete_place(place_id):
        if (place := Place.get_or_none(Place.id == place_id)) is None:
            return {"message": "Place not found"}, 404
        else:
            place.delete_instance()
            return {"message": "Place removed"}, 200

    return app
