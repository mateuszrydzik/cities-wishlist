from flask import Flask, render_template, jsonify
from flask_cors import cross_origin, CORS
from models import database, User, Place
from peewee import fn
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')
# CORS(app)

database.init(app.config['DBNAME'], host=app.config['DBHOST'], user = app.config['DBUSER'], password = app.config['DBPASS'])
# database.create_tables([User])

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/place')
@cross_origin(origins=['http://localhost:3000'])
def get_place():
    places = Place.select(
        fn.ST_AsGeoJSON(Place.geom).alias('geom'),
        Place
    ).dicts()
    features = []
    for row in places:
        geom = row.pop('geom')
        features.append({
            "type":"Feature",
            "geometry":json.loads(geom),
            "properties":row
        })
    return jsonify({
        "type":"FeatureCollection",
        "features":features
        })

if __name__ == '__main__':
    debug=True
    app.run(debug=True)