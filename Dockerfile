FROM python:3.6.2

RUN git clone https://github.com/conanfanli/docs.git /app
WORKDIR /app
RUN git checkout develop && git pull

RUN pip3 install ansible
RUN make play
