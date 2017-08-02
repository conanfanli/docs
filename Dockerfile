FROM python:3.6.2

RUN ln -sf /bin/bash /bin/sh

RUN pip3 install ansible

# RUN git clone https://github.com/conanfanli/docs.git /app
WORKDIR /app
# RUN git checkout develop && git pull

ADD . /app

CMD make play
