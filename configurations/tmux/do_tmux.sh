#!/bin/sh

if [ ! -f "$HOME/.tmux.conf" ]
then
    cp ~/docs/configurations/tmux/tmux.conf ~/.tmux.conf
    echo copied tmux.conf
fi
