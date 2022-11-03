
FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y python3-pip build-essential manpages-dev libpq-dev default-libmysqlclient-dev

RUN python3 -m pip install -U pip \
    && pip3 install mysqlclient \
    && pip3 install --upgrade setuptools \
    && pip3 install -r /app/requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "--timeout", "120", "--max-requests", "600", "--log-file", "-", "truesight.wsgi:application"]