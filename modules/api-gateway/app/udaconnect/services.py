import json
import requests
from .. import g

def create_location(location_data):
    kafka_data = json.dumps(location_data).encode()
    kafka_producer = g.kafka_producer
    kafka_producer.send("locations", kafka_data)

def get_location(location_id):
    url = f'localhost:6000/api/location/{location_id}'
    return requests.get(url)

def create_person(person_data):
    kafka_data = json.dumps(person_data).encode()
    kafka_producer = g.kafka_producer
    kafka_producer.send("persons", kafka_data)

def get_person(person_id):
    url = f'localhost:7000/api/persons/{person_id}'
    return requests.get(url)

def get_persons():
    url = 'localhost:7000/api/persons'
    return requests.get(url)

def find_connections(person_id):
    url = f'localhost:8000/api/connections/{person_id}'
    return requests.get(url)