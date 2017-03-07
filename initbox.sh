#!/bin/bash
set -e

sudo apt-get update
wget -O bootstrap_salt.sh https://bootstrap.saltstack.com
sudo sh bootstrap_salt.sh
sudo apt-get update && sudo apt-get install -y git < "/dev/null";

sudo mkdir -p /home/ubuntu/projects
cd /home/ubuntu/projects

# Clone iconfigs if not exists
test -d iconfigs || sudo git cloneh ttps://gitlab.com/vanillarice/iconfigs.git

# Symlink
sudo mkdir -p /srv/salt
sudo ln -s /home/ubuntu/projects/iconfigs /srv/salt/iconfigs

# Apply salt
sudo salt-call --local state.apply iconfigs

# Change owner
sudo chown -R ubuntu:ubuntu /home/ubuntu/
sudo chown -R ubuntu:ubuntu /srv/salt
