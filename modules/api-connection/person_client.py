import logging
import asyncio
import grpc

import person_pb2
import person_pb2_grpc

# NOTE(gRPC Python Team): .close() is possible on a channel and should be
# used in circumstances in which the with statement does not fit the needs
# of the code.
async with grpc.aio.insecure_channel('localhost:50051') as channel:
    stub = person_pb2_grpc.GreeterStub(channel)
    response = await stub.Get(person_pb2.PersonId(id='you'))
print("Greeter client received: " + response.message)


