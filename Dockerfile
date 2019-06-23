FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV PROJECT_NAME=template
ENV API_ROOT=/web/${PROJECT_NAME}/api

SHELL ["/bin/bash", "-c"]
RUN mkdir /web
RUN mkdir /web/${PROJECT_NAME}
RUN mkdir /web/${PROJECT_NAME}/api
RUN mkdir /web/${PROJECT_NAME}/ui
RUN mkdir /web/${PROJECT_NAME}/config
RUN mkdir /web/${PROJECT_NAME}/media
ADD . ${API_ROOT}
WORKDIR ${API_ROOT}
RUN ls
RUN pip install -r requirements.txt
