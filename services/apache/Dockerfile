###########################################################################
# Dockerfile for apache flask server
###########################################################################

# Set the base image:
FROM ubuntu:18.04

MAINTAINER Twister Team

RUN apt-get update &&\
    apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 \
    python3 python3-pip python3-mysqldb \
    vim curl \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workdir/
COPY requirements.txt /workdir/
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install -r /workdir/requirements.txt

COPY ./www /var/www
COPY ./httpd_conf /etc/apache2/
COPY ./business /workdir/

EXPOSE 80
CMD apachectl -D FOREGROUND