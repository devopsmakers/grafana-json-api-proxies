FROM python:3.9-slim

RUN mkdir /app
COPY ./requirements.txt /app/
RUN apt-get update \
  && apt-get -y install build-essential \
  && cd /app \
  && pip install -r requirements.txt \
  && apt-get clean autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/
COPY ./app.py /app/
COPY ./uwsgi.ini /app/

RUN adduser app --system --uid 1337
USER app

WORKDIR /app

EXPOSE 5000
CMD uwsgi /app/uwsgi.ini