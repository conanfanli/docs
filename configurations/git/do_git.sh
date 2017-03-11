#!/bin/sh -e

CONFIG_FILE="$HOME/docs/configurations/git/gitconfig"
cp $CONFIG_FILE ~/.gitconfig
cat ~/.gitconfig

https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
