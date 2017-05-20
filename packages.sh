#!/bin/bash -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -d ~/.fzf ]
then
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    yes | ~/.fzf/install
fi

if [ ! -f ~/z.sh ]
then
    curl https://raw.githubusercontent.com/rupa/z/master/z.sh > ~/bin/z.sh
fi

$DIR/check_sys.sh

install_ag () {

    if command -v ag > /dev/null 2>&1;
    then
        echo ag is already installed
        return
    fi

    os=`cat data/os`
    if [ "$os" == "centos" ]; then
        sudo yum install epel-release.noarch the_silver_searcher;
    elif [ "$os" == "ubuntu" ]; then
        sudo apt-get install silversearcher-ag;
    elif [ "$os" == "mac" ]; then
        brew install the_silver_searcher;
    else
        echo not supported OS $os;
        exit 1;
    fi
}


install_ag

