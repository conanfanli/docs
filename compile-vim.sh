#!/bin/sh

set -e 
VIM_VERSION=${VIM_VERSION:-7.4.898}

(vi --version | grep '+python3') && echo Already support python 3. Will not compile. && exit 0
sudo apt-get update && sudo apt-get install -y unzip ncurses-dev libx11-dev libxtst-dev libxt-dev libsm-dev libxpm-dev

wget https://github.com/vim/vim/archive/v7.4.898.zip -O /tmp/${VIM_VERSION}.zip

cd /tmp && unzip ${VIM_VERSION} && cd ${VIM_VERSION} && \
    ./configure --with-features=huge --enable-python3interp=dynamic --enable-cscope --prefix=${HOME} && \
    make && \
    make install && \
    sudo ln -s ${HOME}/bin/vim /usr/bin/vi -f

exit 0
