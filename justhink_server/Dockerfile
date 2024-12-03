FROM python:3.12-alpine

COPY ./requirements /requirements
RUN pip install -r requirements/dev.txt
RUN rm -rf requirements

COPY ./justhink/ .
WORKDIR /justhink_server

CMD python manage.py migrate \
 && python manage.py collectstatic --noinput \
 && python manage.py createadmin \
 && gunicorn config.wsgi:application --bind 0.0.0.0:$BACKEND_PORT
