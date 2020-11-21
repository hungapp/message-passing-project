from kafka import KafkaConsumer
import requests
import threading
import logging
import json

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'kafka:9092'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-api")

def poll():
        consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
        for message in consumer:
            payload = message.value.decode('UTF-8', 'strict')
            logger.info(payload)
            response = requests.post(
                url='http://udaconnect-api-location:5000/api/locations-kafka',
                json=json.loads(payload)
                )
            logger.info(response.status_code)
            logger.info(response.reason)

def main():
    t1 = threading.Thread(target=poll)
    t1.start()
    logger.info("started a background thread")

if __name__ == '__main__':
    main()