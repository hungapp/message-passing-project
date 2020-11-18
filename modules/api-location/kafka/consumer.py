from kafka import KafkaConsumer
import requests

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'kafka:9092'

def poll():
        consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
        for message in consumer:
            print(message)
            requests.post('localhost:6000/api/locations-kafka', data = message)

def main():
    t1 = threading.Thread(target=poll)
    t1.start()
    logging.warning("started a background thread")

if __name__ == '__main__':
    main()