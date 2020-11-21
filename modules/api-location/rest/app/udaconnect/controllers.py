import logging
from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)
from app.udaconnect.services import LocationService
from flask import request, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api")

@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> None:
        request_body = request.json
        LocationService.forward(request_body)
        return Response(status=202)

    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

@api.route("/locations-kafka")
class LocationKafkaResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        logger.info(request.get_json())
        location: Location = LocationService.create(request.get_json())
        return location