#!/bin/bash
tmate -S /tmp/tmate.sock new-session -d

set -e
cd ~/dropbox/tmates
git pull
local_machine_name=`cat ~/dropbox/tmates/local_machine_name`
tmate -S /tmp/tmate.sock display -p '#{tmate_web}' > ~/dropbox/tmates/$local_machine_name
git add -A
git commit -m "drop tmate session $local_machine_name"
git push
