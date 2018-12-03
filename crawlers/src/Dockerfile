# Dockerfile for web crawlers

FROM selenium/standalone-chrome:3.11

USER root

RUN apt-get update &&\
    apt-get install -y curl python3 python3-pip &&\
    apt-get clean &&\
    apt-get autoremove &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /workdir/
COPY ./ /workdir/
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install -r /workdir/requirements.txt

ENV PYTHONPATH ${PYTONPATH}:/workdir

CMD ["python3", "/workdir/run.py"]
