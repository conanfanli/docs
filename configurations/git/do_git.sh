#!/bin/sh -e

GIT_CONFIG_DIR="$HOME/docs/configurations/git"
COMPLETION_FILE_PATH="$GIT_CONFIG_DIR/git-completion.bash"
CONFIG_FILE="$GIT_CONFIG_DIR/gitconfig"
cp $CONFIG_FILE ~/.gitconfig

echo Installed gitconfig
cat ~/.gitconfig


# On Linux
if [ -d "/etc/bash_completion.d" ]
then
    ls /etc/bash_completion.d/git-* 1> /dev/null 2>&1 && echo git completion already exists || sudo cp $COMPLETION_FILE_PATH /etc/bash_completion.d/
    ls /etc/bash_completion.d/git-*
    exit 0
fi

# On Mac
if [ -d "/usr/local/etc/bash_completion.d/" ] && [ ! -f "/usr/local/etc/bash_completion.d/git-completion.bash" ]
then
    echo 1111111
fi
