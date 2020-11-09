from concurrent import futures
import logging
import time
import grpc

import person_pb2
import person_pb2_grpc

from wsgi import app
from app.udaconnect.services import PersonService

class PersonGrpcService(person_pb2_grpc.PersonServiceServicer):

    def GetPerson(self, request, context):
        if request.id:
            with app.app_context():
                person = PersonService().retrieve(person_id=request.id)
                logging.debug(person)
                if person:
                    return person_pb2.Person(
                        first_name=person.first_name,
                        last_name=person.last_name,
                        company_name=person.company_name
                    )

    def GetPersons(self, request, context):
        with app.app_context():
            for person in PersonService().retrieve_all():
                yield person_pb2.Person(
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name
                )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonGrpcService(), server)

    logging.info('GRPC running')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
