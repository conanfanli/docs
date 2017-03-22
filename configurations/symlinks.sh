#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ln -is $DIR/bash/bash_profile.bash ~/.bash_profile
ln -is $DIR/git/gitconfig ~/.gitconfig
ln -is $DIR/tmux/tmux.conf ~/.tmux.conf
ln -is $DIR/vim/vimrc ~/.vimrc
