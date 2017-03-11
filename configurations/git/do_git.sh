#!/bin/sh -e

CONFIG_FILE="$HOME/docs/configurations/git/gitconfig"
cp $CONFIG_FILE ~/.gitconfig

echo Installed gitconfig
cat ~/.gitconfig
