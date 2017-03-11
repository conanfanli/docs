#!/bin/sh

mkdir -p ~/docs/data
cd ~/docs

if [ -f "/usr/bin/sw_vers" ]
then
    echo You are on Mac
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
