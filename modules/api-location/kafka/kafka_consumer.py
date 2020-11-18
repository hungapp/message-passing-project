from kafka import KafkaConsumer
import threading
import json
import logging

BOOTSTRAP_SERVERS = ['kafka:9092']

def kafka_listener(data):
    logging.warning( data.value.decode("utf-8"))

def register_kafka_listener(topic, listener=kafka_listener):
    def poll():
        consumer = KafkaConsumer(topic, group_id=1, bootstrap_servers=BOOTSTRAP_SERVERS)
        print("About to start polling for topic:", topic)
        consumer.poll(timeout_ms=500)
        print("Started Polling for topic:", topic)
        for msg in consumer:
            listener(msg)

    logging.warning(f"About to register listener to topic: {topic}")
    t1 = threading.Thread(target=poll)
    t1.start()
    logging.warning("started a background thread")

