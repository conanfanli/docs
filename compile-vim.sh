#!/bin/bash

set -e


usage() {
    echo 'Compile vim using python2 or python3'
    echo './compile-vim.sh [python2|python3]'
    exit 1
}

if [ "$1" == "python2" ]
then
    compile_arg='--enable-pythoninterp=dynamic'
    echo Compiling with Python 2 ...
elif [ "$1" == "python3" ]
then
    compile_arg='--enable-python3interp=dynamic'
    echo Compiling with Python 3 ...
else
    usage
fi


install-vim () {
    (~/bin/vim --version | grep -o 'IMproved 8.0') && echo 'Your Vim is already up to date' && return 0

    sudo apt-get update && sudo apt-get install -y make unzip ncurses-dev libx11-dev libxtst-dev libxt-dev libsm-dev libxpm-dev

    cd ~
    test -d vim || git clone https://github.com/vim/vim.git

    # sudo ln doesn't work on Mac because of permission
    cd vim/src && \
    ./configure --with-features=huge ${compile_arg} --enable-cscope --prefix=${HOME} && \
        make && \
        make install && \
        ln -fs ${HOME}/bin/vim /usr/bin/vim
}

install-vim-plug () {
    if [ ! -f ~/.vim/autoload/plug.vim ]
    then
        curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
        echo Installed vim-plug
    else
        echo Vim-plug already installed
    fi
}


install-vim
install-vim-plug
