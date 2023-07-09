FROM python:3.11

WORKDIR /gabriel

RUN apt-get update && apt-get install -y python3-pip
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

#EXPOSE 8000 #when using traefik not needed

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]