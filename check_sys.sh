#!/bin/sh

mkdir -p ~/docs/data
cd ~/docs

if [ -f "/usr/bin/sw_vers" ]
then
    echo Mac version: $mac
    echo mac > data/os
    exit 0
fi

centos=`cat /etc/*-release | grep -i ubuntu`
if [ -n "$centos" ]
then
    echo You are on Ubuntu
    echo ubuntu > data/os
    exit 0
fi


centos=`cat /etc/*-release | grep -i centos`
if [ -n "$centos" ]
then
    echo You are on CentOS
    echo centos > data/os
    exit 0
fi

# info=`cat /etc/*-release`
# echo $info
# set -e
# VIM_VERSION=${VIM_VERSION:-7.4.898}
#
# (vi --version | grep '+python3') && echo Already support python 3. Will not compile. && exit 0
# sudo apt-get update && sudo apt-get install -y unzip ncurses-dev libx11-dev libxtst-dev libxt-dev libsm-dev libxpm-dev
#
# wget https://github.com/vim/vim/archive/v7.4.898.zip -O /tmp/vim-${VIM_VERSION}.zip
# cd /tmp
# test -d vim-${VIM_VERSION} || unzip vim-${VIM_VERSION}
# cd vim-${VIM_VERSION} && \
#     ./configure --with-features=huge --enable-python3interp=dynamic --enable-cscope --prefix=${HOME} && \
#     make && \
#     make install && \
#     sudo ln -s ${HOME}/bin/vim /usr/bin/vi -f
