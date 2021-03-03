FROM python:3
FROM ubuntu:focal
FROM golang:1.16.0-buster

ADD main.py /
ADD errite/ /errite/
ADD config.json /
RUN pip3 install paramiko
RUN apt install git openssh-server nano
CMD [ "python3", "./monitorSystem.py" ]
