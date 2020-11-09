from datetime import datetime

from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)

from flask import request, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
from .services import create_location, get_location, create_person, get_persons, get_person, find_connections

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self):
        payload = request.get_json()
        create_location(payload)
        return Response(status=201)

    @responds(schema=LocationSchema)
    def get(self, location_id):
        result = get_location(location_id)
        return Response(result.content)


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self):
        payload = request.get_json()
        create_person(payload)
        return Response(status=201)

    @responds(schema=PersonSchema, many=True)
    def get(self):
        result = get_persons()
        return result.content


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id):
        result = get_person(person_id)
        return result.content


@api.route("/connections/<person_id>")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        result = find_connections(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return result.content
