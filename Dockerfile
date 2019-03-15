FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

ADD requirements.txt /code
WORKDIR /code
RUN pip install -r requirements.txt
