FROM python:3.12-alpine

COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
RUN rm -rf requirements

WORKDIR /usr/src/app
COPY ./justhink/ .

CMD python manage.py migrate \
 && python manage.py collectstatic --noinput \
 && gunicorn justhink.wsgi:application --bind 0.0.0.0:$BACKEND_PORT
 