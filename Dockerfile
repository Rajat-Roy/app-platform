# pull official base image
FROM python:3.7-buster

# set work directory
#WORKDIR /usr/src/project

RUN mkdir /src
WORKDIR /src
RUN mkdir assets
RUN mkdir media
RUN mkdir static

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME /root

# install psycopg2
RUN apt-get update 


# install dependencies
COPY ./requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -f requirements.txt
#https://github.com/infoscout/django-cache-utils/issues/12
RUN pip install git+https://github.com/infoscout/django-cache-utils.git@2.0.0
RUN apt-get install -y cron
ADD ./ /src
# run entrypoint.sh
# CMD gunicorn TaxiTrip.wsgi -b 0.0.0.0:8080 --reload --timeout 120
CMD service cron start; python manage.py crontab add; python manage.py runserver 0.0.0.0:8080 --noreload & python manage.py run_huey;
