FROM person-rest:latest as build
WORKDIR /usr/src/grpc
RUN apk add --update  --no-cache libstdc++ libc6-compat openssh-client git gcc cython linux-headers make musl-dev python3-dev g++
COPY . /usr/src/grpc
RUN pip install -r requirements.txt
ENV PYTHONPATH /usr/src/grpc:/usr/src/rest

EXPOSE 50051

CMD [ "python", "main.py" ]