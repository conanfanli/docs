#!/bin/bash
cd ~/dropbox
echo "$(date): $(git pull)" >> /tmp/update_dropbox.log
