from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_restx import Api
from kafka import KafkaProducer
import requests

def create_app(env=None):
    from app.routes import register_routes

    app = Flask(__name__)
    api = Api(app, title="UdaConnect API Gateway", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)

    @app.before_request
    def before_request():
        # Set up Kafka Producer
        KAFKA_SERVER = 'kafka:9092'
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        g.kafka_producer = producer

    @app.route("/health")
    def health():
        location_url = 'localhost:6000/health'
        person_url = 'localhost:7000/health'
        return requests.get(location_url)
        # return jsonify("healthy")

    return app
