from app.udaconnect.services import PersonService

from wsgi import app
import person_pb2
import person_pb2_grpc

class PersonGrpcService(person_pb2_grpc.PersonServiceServicer):

    def GetPerson(self, request, context):
        if request.id:
            with app.app_context():
                person = PersonService().retrieve(person_id=request.id)
                logging.debug(person)
                if person:
                    return person_pb2.PersonResponse(
                        id=person.id,
                        first_name=person.first_name,
                        last_name=person.last_name,
                        company_name=person.company_name
                    )

    def GetPersons(self, request, context):
        with app.app_context():
            for person in PersonService().retrieve_all():
                yield person_pb2.PersonResponse(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name
                )