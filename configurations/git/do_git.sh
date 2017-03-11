#!/bin/sh -e

CONFIG_FILE="$HOME/docs/configurations/git/gitconfig"
cp $CONFIG_FILE ~/.gitconfig

echo Installed gitconfig
cat ~/.gitconfig

(ls /etc/bash_completion.d/ | grep git) && echo 11111 || echo 2222
