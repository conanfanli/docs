#!bin/bash
set -e

sudo apt-get update && sudo apt-get -y install curl

curl -L https://bootstrap.saltstack.com | sudo sh -s -- stable

cd /home/ubuntu/
mkdir -p projects
cd projects

# Clone iconfigs if not exists
test -d iconfigs || git clone https://conanfanli@bitbucket.org/conanfanli/iconfigs.git

# Symlink
sudo mkdir -p /srv/salt
sudo ln -s /home/ubuntu/projects/iconfigs /srv/salt/iconfigs

# Change owner
sudo chown -R ubuntu:ubuntu /home/ubuntu/
sudo chown -R ubuntu:ubuntu /srv/salt

# Apply salt
sudo salt-call --local state.apply iconfigs
