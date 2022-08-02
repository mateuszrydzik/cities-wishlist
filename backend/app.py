from flask_cors import CORS
from flask import Flask, render_template, jsonify, request
from flask_cors import cross_origin
from models import database, User, Place
from configmodule import TestingConfig
from peewee import fn
from shapely.geometry import shape
import json

app = Flask(__name__)
app.config.from_object(TestingConfig())

CORS(app, resoucers={r"/*": {"origins": "*"}})


database.init(app.config['DBNAME'], host=app.config['DBHOST'],
              user=app.config['DBUSER'], password=app.config['DBPASS'],
              port=app.config['DBPORT'])


def create_tables():
    with database:
        database.ceate_tables([User, Place])


@app.route('/login')
def login():
    return render_template('login.html')


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
    return jsonify({
        "type": "FeatureCollection",
        "features": features
    })


@app.route('/places', methods=['POST'])
def add_place():
    req = request.json
    geometry = 'SRID=4326;{}'.format(shape(req['geom']).wkt)
    Place.create(city=req['city'], country=req['country'],
                 notes=req['notes'], geom=geometry)
    return {"status": "added"}


@app.route('/places/<int:point_id>', methods=['DELETE'])
def delete_place(point_id):
    if (point := Place.get_or_none(Place.id == point_id)) is None:
        return {"message": "Point not found"}
    else:
        point.delete_instance()
        return {"message": "Point removed"}


if __name__ == '__main__':
    app.run(debug=True)
