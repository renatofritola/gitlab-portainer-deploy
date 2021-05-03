FROM python:3.9-slim

ADD . /app
WORKDIR /app
RUN python /app/setup.py install

CMD deploy
