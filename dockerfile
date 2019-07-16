FROM ubuntu:16.04

# Changing working directory
WORKDIR /opt/app


COPY code/requirements.txt /opt/app/requirements.txt
RUN  apt-get -yq update



RUN apt-get -y install python-dev && \
    apt-get -y install python-pip && \
    apt-get -y install libxml2-dev && \
    apt-get -y install libxslt1-dev && \
    apt-get -y install zlib1g-dev && \
    apt-get -y install libffi-dev && \
    apt-get -y install libssl-dev && \
    apt-get -y install build-essential && \
    apt-get -y install libenchant1c2a

# Install requirements.txt


RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir assay

WORKDIR /opt/app/assay/code
RUN ["python", "start.py"]
