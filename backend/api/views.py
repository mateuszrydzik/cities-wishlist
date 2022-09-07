from flask import Blueprint, request
from flask.views import MethodView, View
from peewee import fn
from shapely.geometry import shape
import json
from api.models import Place
from flasgger import swag_from


def class_route(self, rule, endpoint, model):

    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint, model))
        return cls

    return decorator


places_bp = Blueprint("places_bp", __name__)


@class_route(places_bp, "/status", "status", Place)
class StatusView(View):
    def __init__(self, model):
        self.model = model

    @swag_from('docs/status.yml')
    def dispatch_request(self):
        if (self.model.get_or_none()) is None:
            return {"message": "Not connected"}, 404
        else:
            return {"message": "Connected"}


@class_route(places_bp, "/places/<int:place_id>", "places-item", Place)
class ItemAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    @swag_from('docs/get_place_id.yml')
    def get(self, place_id):
        if (self.model.get_or_none(self.model.id == place_id)) is None:
            return {"message": "Not found"}
        else:
            place = self.model.select(
                fn.ST_AsGeoJSON(self.model.geom).alias('geom'),
                self.model
            ).where(
                self.model.id == place_id
            ).dicts().get()
        return {
            "type": "Feature",
            "geometry": json.loads(place.pop('geom')),
            "properties": place
        }

    @swag_from('docs/put_place.yml')
    def put(self, place_id):
        if (place := self.model.get_or_none(
                self.model.id == place_id)) is None:
            return {"message": "Not found"}, 404
        else:
            place.notes = request.args.get('notes')
            place.save()
            return {"message": "Updated"}

    @swag_from('docs/delete_place.yml')
    def delete(self, place_id):
        if (place := self.model.get_or_none(
                self.model.id == place_id)) is None:
            return {"message": "Place not found"}, 404
        else:
            place.delete_instance()
            return {"message": "Removed"}


@class_route(places_bp, "/places", "places-group", Place)
class GroupAPI(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    @swag_from('docs/get_places.yml')
    def get(self):
        places = self.model.select(
            fn.ST_AsGeoJSON(self.model.geom).alias('geom'),
            self.model
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

    @swag_from('docs/post_place.yml')
    def post(self):
        req = request.json
        geom = 'SRID=4326;{}'.format(shape(req['geom']).wkt)
        self.model.create(
            city=req['city'],
            country=req['country'],
            notes=req['notes'],
            geom=geom
        )
        return {"message": "Place added"}
