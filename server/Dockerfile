FROM python:3.9-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements/ /server/requirements/
RUN pip install pip-tools
RUN pip-sync requirements/development.txt

COPY ./server /server
