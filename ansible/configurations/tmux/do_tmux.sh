#!/bin/sh

if [ ! -f "$HOME/.tmux.conf" ]
then
    cp ~/rice/configurations/tmux/tmux.conf ~/.tmux.conf
    echo copied tmux.conf
fi
