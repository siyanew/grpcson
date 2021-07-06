FROM python:3.9-buster

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y wget

RUN pip install -U pip
ADD requirements.txt /usr/requirements.txt
RUN pip install -r /usr/requirements.txt

RUN wget https://github.com/fullstorydev/grpcurl/releases/download/v1.8.1/grpcurl_1.8.1_linux_x86_64.tar.gz
RUN tar xf grpcurl_1.8.1_linux_x86_64.tar.gz -C /bin/

ADD . /usr/grpcon
WORKDIR /usr/grpcon

ENTRYPOINT ["python", "src/app.py"]

