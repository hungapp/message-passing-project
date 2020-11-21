from concurrent import futures
import logging
import time
import grpc

import person_pb2_grpc
from service import PersonGrpcService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonGrpcService(), server)

    print('GRPC running')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
