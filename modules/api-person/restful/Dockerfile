FROM python:3.7-alpine

WORKDIR /usr/src/app/restful

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app/restful
ENV PYTHONPATH /usr/src/app/restful

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]