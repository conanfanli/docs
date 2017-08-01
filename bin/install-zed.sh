#!/bin/bash
if [ ! -f ~/bin/z.sh ]
then
    mkdir -p ~/bin
    curl https://raw.githubusercontent.com/rupa/z/master/z.sh > ~/bin/z.sh
fi
