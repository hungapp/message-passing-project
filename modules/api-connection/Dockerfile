FROM python:3.7-alpine

WORKDIR .

RUN apk add --update  --no-cache libstdc++ libc6-compat openssh-client git gcc cython linux-headers make musl-dev python3-dev g++ geos libc-dev postgresql-dev
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]