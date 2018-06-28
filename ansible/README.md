# Setup a new box
- clone this repo
- Install ansible: `sudo apt-get update && sudo apt install -y python python3 python3-pip && sudo pip3 install ansible`
- Make sure you're a sudoer without password. To do so, add your username to `/etc/sudoers`. For example: `john ALL=(ALL) NOPASSWD:ALL`

## Run the whole thing
- `cd ansible && make play`

## Run specific tags
- `make play-tags vim tmux`
- Tasks are defined [here](https://github.com/conanfanli/rice/tree/master/ansible/roles/common/tasks)

