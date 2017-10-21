#!/bin/bash -e

(vim --version | grep -o 'IMproved 8.0') && echo 'Your Vim is already up to date' && exit 0

apt-get update && apt-get install -y make unzip ncurses-dev libx11-dev libxtst-dev libxt-dev libsm-dev libxpm-dev

cd /tmp
test -d vim || git clone https://github.com/vim/vim.git

cd vim/src && \
    ./configure --with-features=huge --enable-python3interp=dynamic --enable-cscope && \
    make && \
    make install
