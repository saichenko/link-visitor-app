FROM python:3.9-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements/development.txt /server/
RUN pip install pip-tools
RUN pip-sync development.txt

COPY ./server /server

RUN python ./manage.py collectstatic --noinput

#########################################

FROM nginx:1.17.8

RUN rm -v /etc/nginx/nginx.conf
COPY ./nginx/nginx.conf /etc/nginx/

RUN mkdir /nginx
COPY --from=server /server/staticfiles /nginx/static
