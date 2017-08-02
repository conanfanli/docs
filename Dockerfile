FROM python:3.6.2

# Install locales
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8

RUN ln -sf /bin/bash /bin/sh

RUN pip3 install ansible

# RUN git clone https://github.com/conanfanli/docs.git /app
WORKDIR /app
# RUN git checkout develop && git pull

ADD . /app

RUN make play -- --tags bash

CMD make play
