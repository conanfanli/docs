#!bin/bash
set -e
echo -n Please enter your password for iconfigs: 
read -s password

curl -L https://bootstrap.saltstack.com | sudo sh -s -- stable
sudo apt-get update && sudo apt-get install -y git < "/dev/null";

cd /home/ubuntu/
sudo mkdir -p projects
cd projects

# Clone iconfigs if not exists
test -d iconfigs || sudo git clone https://conanfanli:$password@bitbucket.org/conanfanli/iconfigs.git

# Symlink
sudo mkdir -p /srv/salt
sudo ln -s /home/ubuntu/projects/iconfigs /srv/salt/iconfigs

# Change owner
sudo chown -R ubuntu:ubuntu /home/ubuntu/
sudo chown -R ubuntu:ubuntu /srv/salt

# Apply salt
sudo salt-call --local state.apply iconfigs
