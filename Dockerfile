FROM ubuntu:focal
ENV TZ America/Chicago
RUN apt update
RUN apt install -y tzdata
ADD main.py /
ADD errite/ /errite/
ADD config.json /
RUN apt install git openssh-server nano python3-pip golang -y
RUN pip3 install paramiko
CMD [ "python3", "./main.py" ]
