FROM python:3.6.2

RUN ln -sf /bin/bash /bin/sh

ENV TERM xterm

RUN apt-get update

# Install locales
# RUN apt-get clean && apt-get update && apt-get install -y locales
# RUN locale-gen en_US.UTF-8 && update-locale
# ENV LANG en_US.UTF-8

RUN pip3 install ansible

RUN mkdir /root/rice
# RUN git clone https://github.com/conanfanli/rice.git /app
WORKDIR /root/rice
# RUN git checkout develop && git pull

ADD . /root/rice

RUN make play -- --tags bash

CMD make play
