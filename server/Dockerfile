FROM python:3.9-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements/development.txt /server/
RUN pip install pip-tools
RUN pip-sync development.txt

COPY ./server /server
