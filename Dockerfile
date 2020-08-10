FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
ADD requirements.txt /backend/

WORKDIR /backend


RUN pip install -r requirements.txt
ADD . /backend/
