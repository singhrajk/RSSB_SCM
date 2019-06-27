FROM selenium/standalone-chrome-debug:latest

COPY src/ /opt/src/

COPY build.py /opt/

RUN sudo apt-get update && sudo apt-get install -y python-pip

RUN pip install selenium

WORKDIR /opt/

ARG SITE_LOGIN_USER

ENV SITE_LOGIN_USER=$SITE_LOGIN_USER

ARG SITE_LOGIN_PWD

ENV SITE_LOGIN_PWD=$SITE_LOGIN_PWD

ARG CMD_EXECUTOR

ENV CMD_EXECUTOR=$CMD_EXECUTOR
