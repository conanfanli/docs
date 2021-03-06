#!/bin/sh

mkdir -p ~/rice/data
cd ~/rice

if [ -f "/usr/bin/sw_vers" ]
then
    echo You are on Mac
    echo mac > data/os
    exit 0
fi

ubuntu=`cat /etc/*-release | grep -i ubuntu`
if [ -n "$ubuntu" ]
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

echo unknown OS
exit 1
